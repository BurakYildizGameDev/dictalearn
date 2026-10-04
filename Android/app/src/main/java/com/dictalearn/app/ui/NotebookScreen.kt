package com.dictalearn.app.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.DeleteSweep
import androidx.compose.material.icons.filled.VolumeUp
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.dictalearn.app.domain.dictionary.Dictionary
import com.dictalearn.app.domain.library.LessonCatalog
import com.dictalearn.app.domain.mistakes.MistakeKind
import com.dictalearn.app.domain.mistakes.MistakeRepository
import com.dictalearn.app.domain.review.SrsStore
import com.dictalearn.app.ui.theme.Dicta

private data class NotebookRow(val word: String, val count: Int, val unknown: Boolean, val lessonId: String)

/** Mistake notebook (F3.3): missed words plus words marked as unknown in the word card. */
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun NotebookScreen(
    repository: MistakeRepository,
    dictionary: Dictionary?,
    onSpeak: (String) -> Unit,
    onBack: () -> Unit,
    srs: SrsStore? = null,
    onStartReview: () -> Unit = {}
) {
    var version by remember { mutableIntStateOf(0) }
    var confirmClear by remember { mutableStateOf(false) }
    val rows = remember(version) {
        repository.getMistakes()
            .filter { it.word.isNotBlank() }
            .groupBy { it.word.trim().lowercase() }
            .map { (word, list) ->
                NotebookRow(word, list.size, list.any { it.kind == MistakeKind.UNKNOWN }, list.maxBy { it.timestamp }.lessonId)
            }
            .sortedByDescending { it.count }
    }
    val reviewStats = remember(version) {
        srs?.let {
            it.sync(repository.getMistakes())
            it.stats()
        }
    }

    Scaffold(
        containerColor = Dicta.Background,
        topBar = {
            TopAppBar(
                navigationIcon = {
                    IconButton(onClick = onBack) { Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Geri") }
                },
                title = { Text("Defterim", fontFamily = FontFamily.Serif) },
                actions = {
                    if (rows.isNotEmpty()) {
                        IconButton(onClick = { confirmClear = true }) {
                            Icon(Icons.Default.DeleteSweep, contentDescription = "Defteri temizle")
                        }
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(containerColor = Dicta.Background)
            )
        }
    ) { padding ->
        if (rows.isEmpty()) {
            Box(Modifier.fillMaxSize().padding(padding).padding(32.dp), contentAlignment = Alignment.Center) {
                Text(
                    "Henüz kelime yok. Dikte yaptıkça yanlış yazdığın kelimeler burada birikecek.",
                    color = Dicta.TextMuted
                )
            }
        } else {
            LazyColumn(
                modifier = Modifier.fillMaxSize().padding(padding),
                contentPadding = PaddingValues(16.dp),
                verticalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                if (reviewStats != null && reviewStats.total > 0) {
                    item {
                        Column(
                            modifier = Modifier
                                .fillMaxWidth()
                                .clip(RoundedCornerShape(16.dp))
                                .background(Dicta.Accent.copy(alpha = 0.08f))
                                .padding(16.dp),
                            verticalArrangement = Arrangement.spacedBy(6.dp)
                        ) {
                            Text(
                                if (reviewStats.due > 0) "Bugün tekrar zamanı gelen ${reviewStats.due} kelime var" else "Bugünkü tekrarlar tamam",
                                color = Dicta.TextPrimary,
                                fontSize = 15.sp
                            )
                            Text(
                                "Aralıklı tekrar: bildiğin kelimeler 1, 3, 7, 14, 30 gün arayla sorulur · öğrenilen: ${reviewStats.learned} / ${reviewStats.total}",
                                color = Dicta.TextMuted,
                                fontSize = 12.sp
                            )
                            Button(onClick = onStartReview, enabled = reviewStats.due > 0) { Text("Tekrara başla") }
                        }
                    }
                }
                items(rows, key = { it.word }) { row ->
                    Row(
                        modifier = Modifier
                            .fillMaxWidth()
                            .clip(RoundedCornerShape(14.dp))
                            .background(Dicta.Surface)
                            .padding(horizontal = 8.dp, vertical = 10.dp),
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        IconButton(onClick = { onSpeak(row.word) }) {
                            Icon(Icons.Default.VolumeUp, contentDescription = "${row.word} dinle", tint = Dicta.TextSecondary)
                        }
                        Column(Modifier.weight(1f)) {
                            Text(row.word, fontFamily = FontFamily.Serif, fontSize = 18.sp, color = Dicta.TextPrimary)
                            val meaning = dictionary?.lookup(row.word)?.meaning ?: if (dictionary == null) "…" else "Sözlükte yok"
                            val book = LessonCatalog.find(row.lessonId.removeSuffix("::hard"))?.title
                            Text(
                                listOfNotNull(meaning, book).joinToString(" · "),
                                color = Dicta.TextMuted,
                                fontSize = 12.sp,
                                maxLines = 1,
                                overflow = TextOverflow.Ellipsis
                            )
                        }
                        if (row.unknown) {
                            Text(
                                "bilmiyorum",
                                color = Dicta.Accent,
                                fontSize = 10.sp,
                                modifier = Modifier
                                    .clip(RoundedCornerShape(6.dp))
                                    .background(Dicta.Accent.copy(alpha = 0.1f))
                                    .padding(horizontal = 6.dp, vertical = 2.dp)
                            )
                        }
                        Text("×${row.count}", color = Dicta.Error, fontSize = 12.sp, modifier = Modifier.padding(horizontal = 10.dp))
                    }
                }
            }
        }
    }

    if (confirmClear) {
        AlertDialog(
            onDismissRequest = { confirmClear = false },
            title = { Text("Defter temizlensin mi?") },
            text = { Text("Defterdeki tüm kelimeler silinecek.") },
            confirmButton = {
                TextButton(onClick = {
                    repository.clearMistakes()
                    version++
                    confirmClear = false
                }) { Text("Temizle") }
            },
            dismissButton = { TextButton(onClick = { confirmClear = false }) { Text("Vazgeç") } }
        )
    }
}
