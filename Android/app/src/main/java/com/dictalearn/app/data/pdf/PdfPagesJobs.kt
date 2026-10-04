package com.dictalearn.app.data.pdf

import android.content.Context
import android.graphics.Bitmap
import android.graphics.Color
import android.graphics.pdf.PdfRenderer
import android.os.ParcelFileDescriptor
import com.dictalearn.app.domain.pdflesson.OcrLayout
import com.dictalearn.app.domain.pdflesson.OcrWord
import com.google.mlkit.vision.common.InputImage
import com.google.mlkit.vision.text.TextRecognition
import com.google.mlkit.vision.text.latin.TextRecognizerOptions
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.Job
import kotlinx.coroutines.SupervisorJob
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.ensureActive
import kotlin.coroutines.coroutineContext
import kotlinx.coroutines.launch
import kotlinx.coroutines.tasks.await
import org.json.JSONArray
import org.json.JSONObject
import java.io.File

data class PdfPagesState(
    val pdfId: String,
    val totalPages: Int = 0,
    val texts: List<String?> = emptyList(),
    val running: Boolean = true,
    val error: String? = null
) {
    /** Pages processed from page 1 without a gap. */
    val contiguousDone: Int get() = texts.indexOfFirst { it == null }.let { if (it == -1) texts.size else it }
}

/**
 * Reads every page of a user PDF in order with ML Kit OCR on rendered pages (Android has no
 * built-in PDF text extraction, and rendering + OCR also covers scanned PDFs). Jobs run in an
 * app-wide scope so they continue in the background, and every page is cached on disk.
 */
class PdfPagesJobs(private val context: Context) {
    private companion object {
        const val VERSION = 4
        const val RENDER_WIDTH = 1600
    }

    private val scope = CoroutineScope(SupervisorJob() + Dispatchers.Default)
    private val states = mutableMapOf<String, MutableStateFlow<PdfPagesState>>()
    private val jobs = mutableMapOf<String, Job>()
    private val recognizer by lazy { TextRecognition.getClient(TextRecognizerOptions.DEFAULT_OPTIONS) }
    private val cacheDir = File(context.filesDir, "pdf_pages").apply { mkdirs() }

    @Synchronized
    fun state(pdfId: String, file: File): StateFlow<PdfPagesState> {
        states[pdfId]?.let { flow ->
            if (jobs[pdfId]?.isActive == true || (!flow.value.running && flow.value.error == null)) return flow
        }
        val flow = MutableStateFlow(PdfPagesState(pdfId))
        states[pdfId] = flow
        jobs[pdfId] = scope.launch { run(pdfId, file, flow) }
        return flow
    }

    @Synchronized
    fun cancel(pdfId: String) {
        jobs.remove(pdfId)?.cancel()
        states.remove(pdfId)
        cacheFile(pdfId).delete()
    }

    private suspend fun run(pdfId: String, file: File, flow: MutableStateFlow<PdfPagesState>) {
        try {
            ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY).use { fd ->
                PdfRenderer(fd).use { renderer ->
                    val total = renderer.pageCount
                    val texts: MutableList<String?> = readCache(pdfId, total) ?: MutableList(total) { null }
                    flow.value = flow.value.copy(totalPages = total, texts = texts.toList())
                    for (i in 0 until total) {
                        coroutineContext.ensureActive()
                        if (texts[i] != null) continue
                        texts[i] = recognizePage(renderer, i)
                        writeCache(pdfId, total, texts)
                        flow.value = flow.value.copy(texts = texts.toList())
                    }
                }
            }
            flow.value = flow.value.copy(running = false)
        } catch (e: Exception) {
            flow.value = flow.value.copy(running = false, error = e.message ?: "PDF okunamadı.")
        }
    }

    private suspend fun recognizePage(renderer: PdfRenderer, index: Int): String {
        val bitmap = renderer.openPage(index).use { page ->
            val height = (RENDER_WIDTH.toFloat() * page.height / page.width).toInt()
            Bitmap.createBitmap(RENDER_WIDTH, height, Bitmap.Config.ARGB_8888).also {
                it.eraseColor(Color.WHITE)
                page.render(it, null, null, PdfRenderer.Page.RENDER_MODE_FOR_PRINT)
            }
        }
        try {
            val result = recognizer.process(InputImage.fromBitmap(bitmap, 0)).await()
            val lines = result.textBlocks
                .flatMap { it.lines }
                .mapNotNull { line ->
                    val top = line.boundingBox?.top ?: return@mapNotNull null
                    top to line.elements.mapNotNull { el ->
                        val box = el.boundingBox ?: return@mapNotNull null
                        OcrWord(el.text, box.left, box.right)
                    }
                }
                .sortedBy { it.first }
                .map { it.second }
            return OcrLayout.orderLines(lines, bitmap.width)
        } finally {
            bitmap.recycle()
        }
    }

    private fun cacheFile(pdfId: String) = File(cacheDir, "$pdfId.json")

    private fun readCache(pdfId: String, total: Int): MutableList<String?>? = runCatching {
        val o = JSONObject(cacheFile(pdfId).readText())
        if (o.optInt("version") != VERSION || o.optInt("totalPages") != total) return null
        val arr = o.getJSONArray("texts")
        MutableList(total) { i -> if (arr.isNull(i)) null else arr.getString(i) }
    }.getOrNull()

    private fun writeCache(pdfId: String, total: Int, texts: List<String?>) {
        val arr = JSONArray()
        texts.forEach { arr.put(it ?: JSONObject.NULL) }
        cacheFile(pdfId).writeText(JSONObject().put("version", VERSION).put("totalPages", total).put("texts", arr).toString())
    }
}
