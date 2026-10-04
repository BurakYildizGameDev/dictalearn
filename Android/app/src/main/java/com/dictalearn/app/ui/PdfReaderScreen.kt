package com.dictalearn.app.ui

import android.content.Context
import android.graphics.Bitmap
import android.graphics.Color as AndroidColor
import android.graphics.pdf.PdfRenderer
import android.os.ParcelFileDescriptor
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalConfiguration
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.dictalearn.app.ui.theme.Dicta
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock
import kotlinx.coroutines.withContext
import java.io.File

/** Wraps PdfRenderer (not thread-safe) behind a mutex. */
private class PdfDocument(file: File) {
    private val fd = ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY)
    private val renderer = PdfRenderer(fd)
    private val lock = Mutex()
    val pageCount: Int = renderer.pageCount

    suspend fun render(index: Int, widthPx: Int): Bitmap = lock.withLock {
        withContext(Dispatchers.IO) {
            renderer.openPage(index).use { page ->
                val height = (widthPx.toFloat() * page.height / page.width).toInt()
                val bitmap = Bitmap.createBitmap(widthPx, height, Bitmap.Config.ARGB_8888)
                bitmap.eraseColor(AndroidColor.WHITE)
                page.render(bitmap, null, null, PdfRenderer.Page.RENDER_MODE_FOR_DISPLAY)
                bitmap
            }
        }
    }

    fun close() {
        renderer.close()
        fd.close()
    }
}

/** Assets may be compressed inside the APK; PdfRenderer needs a seekable file. */
private suspend fun copyAssetToCache(context: Context, assetPath: String): File = withContext(Dispatchers.IO) {
    val out = File(context.cacheDir, "pdf/" + assetPath.substringAfterLast('/'))
    if (!out.exists()) {
        out.parentFile?.mkdirs()
        val tmp = File(out.path + ".tmp")
        context.assets.open(assetPath).use { input -> tmp.outputStream().use { input.copyTo(it) } }
        tmp.renameTo(out)
    }
    out
}

/** In-app reader for the book PDFs (Faz 5.9, Android). */
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun PdfReaderScreen(assetPath: String?, title: String, onBack: () -> Unit, localFile: File? = null) {
    val context = LocalContext.current
    var document by remember { mutableStateOf<PdfDocument?>(null) }
    var error by remember { mutableStateOf<String?>(null) }

    LaunchedEffect(assetPath, localFile) {
        try {
            val file = localFile ?: copyAssetToCache(context, requireNotNull(assetPath))
            document = withContext(Dispatchers.IO) { PdfDocument(file) }
        } catch (e: Exception) {
            error = e.message ?: "PDF açılamadı."
        }
    }
    DisposableEffect(Unit) { onDispose { document?.close() } }

    val widthPx = with(LocalDensity.current) { (LocalConfiguration.current.screenWidthDp.dp - 24.dp).roundToPx() }

    Scaffold(
        containerColor = Dicta.Background,
        topBar = {
            TopAppBar(
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Geri")
                    }
                },
                title = {
                    Column {
                        Text(title, maxLines = 1, overflow = TextOverflow.Ellipsis, fontSize = 17.sp)
                        document?.let { Text("${it.pageCount} sayfa", fontSize = 12.sp, color = Dicta.TextMuted) }
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(containerColor = Dicta.Background)
            )
        }
    ) { padding ->
        val doc = document
        when {
            error != null -> Box(Modifier.fillMaxSize().padding(padding), contentAlignment = Alignment.Center) {
                Text(error!!, color = Dicta.Error)
            }
            doc == null -> Box(Modifier.fillMaxSize().padding(padding), contentAlignment = Alignment.Center) {
                CircularProgressIndicator(color = Dicta.Accent)
            }
            else -> LazyColumn(
                modifier = Modifier.fillMaxSize().padding(padding),
                contentPadding = PaddingValues(12.dp),
                verticalArrangement = Arrangement.spacedBy(12.dp)
            ) {
                items((0 until doc.pageCount).toList(), key = { it }) { index ->
                    var bitmap by remember(index) { mutableStateOf<Bitmap?>(null) }
                    LaunchedEffect(index, widthPx) { bitmap = doc.render(index, widthPx) }
                    val bmp = bitmap
                    if (bmp == null) {
                        Box(
                            modifier = Modifier
                                .fillMaxWidth()
                                .aspectRatio(1f / 1.414f)
                                .clip(RoundedCornerShape(6.dp))
                                .background(Color.White.copy(alpha = 0.06f))
                        )
                    } else {
                        Image(
                            bitmap = bmp.asImageBitmap(),
                            contentDescription = "Sayfa ${index + 1}",
                            contentScale = ContentScale.FillWidth,
                            modifier = Modifier
                                .fillMaxWidth()
                                .clip(RoundedCornerShape(6.dp))
                        )
                    }
                }
            }
        }
    }
}
