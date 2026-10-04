package com.dictalearn.app.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.GridItemSpan
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.items
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.Edit
import androidx.compose.material.icons.filled.PlayArrow
import androidx.compose.material.icons.filled.Search
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.dictalearn.app.domain.library.CatalogBook
import com.dictalearn.app.domain.library.LessonCatalog
import com.dictalearn.app.domain.progress.LessonProgress
import com.dictalearn.app.ui.theme.Dicta

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun LibraryScreen(
    books: List<CatalogBook>,
    progress: Map<String, LessonProgress>,
    lastBookId: String?,
    onOpenBook: (CatalogBook) -> Unit,
    onOpenEditor: () -> Unit
) {
    var query by rememberSaveable { mutableStateOf("") }
    var level by rememberSaveable { mutableStateOf<Int?>(null) }

    val visible = remember(books, query, level) { LessonCatalog.filter(books, level, query) }
    val grouped = remember(visible) {
        visible.groupBy { it.level }.toList().sortedBy { (lvl, _) -> if (lvl == 0) 99 else lvl }
    }
    val levels = remember(books) { books.map { it.level }.distinct().sortedBy { if (it == 0) 99 else it } }
    val lastBook = lastBookId?.let { id -> books.firstOrNull { it.id == id } }
    val lastProgress = lastBook?.let { progress[it.id] }

    Scaffold(
        containerColor = Dicta.Background,
        topBar = {
            TopAppBar(
                title = { Text("DictaLearn", fontWeight = FontWeight.SemiBold, fontSize = 18.sp) },
                actions = {
                    IconButton(onClick = onOpenEditor) {
                        Icon(Icons.Default.Edit, contentDescription = "Ders oluştur", tint = Dicta.TextSecondary)
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(containerColor = Dicta.Background)
            )
        }
    ) { padding ->
        LazyVerticalGrid(
            columns = GridCells.Adaptive(minSize = 148.dp),
            modifier = Modifier
                .fillMaxSize()
                .padding(padding),
            contentPadding = PaddingValues(start = 16.dp, end = 16.dp, bottom = 32.dp),
            horizontalArrangement = Arrangement.spacedBy(14.dp),
            verticalArrangement = Arrangement.spacedBy(18.dp)
        ) {
            item(span = { GridItemSpan(maxLineSpan) }) {
                Column(verticalArrangement = Arrangement.spacedBy(14.dp)) {
                    Text(
                        "Dinle. Yaz. Düzelt.",
                        style = MaterialTheme.typography.headlineLarge,
                        color = Dicta.TextPrimary
                    )
                    Text(
                        "${books.count { it.level > 0 }} kademeli klasik. Cümleyi önce kulağınla duy, sonra yaz ve farkları gör.",
                        color = Dicta.TextSecondary,
                        fontSize = 14.sp
                    )
                    if (lastBook != null && lastProgress != null && !lastProgress.completed) {
                        ContinueCard(lastBook, lastProgress) { onOpenBook(lastBook) }
                    }
                    OutlinedTextField(
                        value = query,
                        onValueChange = { query = it },
                        modifier = Modifier.fillMaxWidth(),
                        singleLine = true,
                        placeholder = { Text("Kitap, yazar ara…") },
                        leadingIcon = { Icon(Icons.Default.Search, contentDescription = null) },
                        shape = RoundedCornerShape(14.dp),
                        colors = OutlinedTextFieldDefaults.colors(
                            unfocusedBorderColor = Dicta.Outline,
                            focusedBorderColor = Dicta.Accent,
                            unfocusedContainerColor = Dicta.Surface,
                            focusedContainerColor = Dicta.Surface
                        )
                    )
                    Row(
                        modifier = Modifier.horizontalScroll(rememberScrollState()),
                        horizontalArrangement = Arrangement.spacedBy(8.dp)
                    ) {
                        FilterChip(selected = level == null, onClick = { level = null }, label = { Text("Tümü") })
                        levels.forEach { lvl ->
                            FilterChip(
                                selected = level == lvl,
                                onClick = { level = lvl },
                                label = { Text(LessonCatalog.levelShort[lvl] ?: "$lvl") }
                            )
                        }
                    }
                }
            }

            if (visible.isEmpty()) {
                item(span = { GridItemSpan(maxLineSpan) }) {
                    Text(
                        "“$query” için sonuç yok.",
                        color = Dicta.TextMuted,
                        modifier = Modifier.padding(vertical = 40.dp)
                    )
                }
            }

            grouped.forEach { (lvl, list) ->
                item(span = { GridItemSpan(maxLineSpan) }) {
                    Row(verticalAlignment = Alignment.Bottom, modifier = Modifier.padding(top = 12.dp)) {
                        Text(
                            LessonCatalog.levelLabels[lvl] ?: "Seviye $lvl",
                            style = MaterialTheme.typography.titleLarge,
                            color = Dicta.TextPrimary
                        )
                        Spacer(Modifier.width(8.dp))
                        Text("${list.size} ders", color = Dicta.TextMuted, fontSize = 12.sp)
                    }
                }
                items(list, key = { it.id }) { book ->
                    BookCard(book, progress[book.id]) { onOpenBook(book) }
                }
            }
        }
    }
}

@Composable
private fun BookCover(book: CatalogBook, modifier: Modifier = Modifier, showText: Boolean = true) {
    Box(
        modifier = modifier
            .aspectRatio(3f / 4f)
            .clip(RoundedCornerShape(12.dp))
            .background(Dicta.coverBrush(book.id))
            .padding(10.dp)
    ) {
        Text(
            LessonCatalog.levelShort[book.level] ?: "",
            color = Color.White.copy(alpha = 0.9f),
            fontSize = 10.sp,
            fontWeight = FontWeight.Bold,
            modifier = Modifier
                .align(Alignment.TopEnd)
                .background(Color.Black.copy(alpha = 0.25f), RoundedCornerShape(6.dp))
                .padding(horizontal = 6.dp, vertical = 2.dp)
        )
        if (showText) {
            Column(modifier = Modifier.align(Alignment.BottomStart)) {
                Text(
                    book.title,
                    color = Color.White,
                    fontFamily = FontFamily.Serif,
                    fontSize = 15.sp,
                    lineHeight = 18.sp,
                    maxLines = 4,
                    overflow = TextOverflow.Ellipsis
                )
                Text(
                    book.author.uppercase(),
                    color = Color.White.copy(alpha = 0.7f),
                    fontSize = 9.sp,
                    letterSpacing = 0.8.sp,
                    maxLines = 1,
                    overflow = TextOverflow.Ellipsis
                )
            }
        }
    }
}

@Composable
private fun BookCard(book: CatalogBook, progress: LessonProgress?, onClick: () -> Unit) {
    Column(
        modifier = Modifier
            .clip(RoundedCornerShape(12.dp))
            .clickable(onClick = onClick)
    ) {
        BookCover(book, Modifier.fillMaxWidth())
        Spacer(Modifier.height(8.dp))
        Text(book.title, color = Dicta.TextPrimary, fontSize = 14.sp, fontWeight = FontWeight.Medium, maxLines = 1, overflow = TextOverflow.Ellipsis)
        book.titleTr?.let {
            Text(it, color = Dicta.TextMuted, fontSize = 12.sp, maxLines = 1, overflow = TextOverflow.Ellipsis)
        }
        if (progress?.completed == true) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Icon(Icons.Default.CheckCircle, contentDescription = null, tint = Dicta.Success, modifier = Modifier.size(12.dp))
                Spacer(Modifier.width(4.dp))
                Text("Tamamlandı", color = Dicta.Success, fontSize = 11.sp)
            }
        } else {
            Text(
                if (book.level > 0) "${book.pages} sayfa · ${book.sentences} cümle" else "${book.sentences} cümle",
                color = Dicta.TextMuted,
                fontSize = 11.sp
            )
            if (progress != null && progress.percent > 0) {
                Spacer(Modifier.height(6.dp))
                LinearProgressIndicator(
                    progress = { progress.percent / 100f },
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(3.dp)
                        .clip(CircleShape),
                    color = Dicta.Accent,
                    trackColor = Dicta.SurfaceHigh
                )
            }
        }
    }
}

@Composable
private fun ContinueCard(book: CatalogBook, progress: LessonProgress, onClick: () -> Unit) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(16.dp))
            .background(Dicta.Surface)
            .border(1.dp, Dicta.Outline, RoundedCornerShape(16.dp))
            .clickable(onClick = onClick)
            .padding(12.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        BookCover(book, Modifier.width(48.dp), showText = false)
        Spacer(Modifier.width(12.dp))
        Column(Modifier.weight(1f)) {
            Text("KALDIĞIN YERDEN DEVAM ET", style = MaterialTheme.typography.labelSmall, color = Dicta.Accent)
            Text(book.title, fontFamily = FontFamily.Serif, fontSize = 17.sp, color = Dicta.TextPrimary, maxLines = 1, overflow = TextOverflow.Ellipsis)
            Text("Cümle ${progress.segmentIndex + 1} / ${progress.totalSegments}", color = Dicta.TextMuted, fontSize = 12.sp)
            Spacer(Modifier.height(6.dp))
            LinearProgressIndicator(
                progress = { progress.percent / 100f },
                modifier = Modifier
                    .fillMaxWidth()
                    .height(3.dp)
                    .clip(CircleShape),
                color = Dicta.Accent,
                trackColor = Dicta.SurfaceHigh
            )
        }
        Spacer(Modifier.width(12.dp))
        Box(
            modifier = Modifier
                .size(40.dp)
                .clip(CircleShape)
                .background(Dicta.AccentStrong),
            contentAlignment = Alignment.Center
        ) {
            Icon(Icons.Default.PlayArrow, contentDescription = "Devam et", tint = Color.White)
        }
    }
}
