package com.dictalearn.app.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.BookmarkAdd
import androidx.compose.material.icons.filled.Check
import androidx.compose.material.icons.filled.Translate
import androidx.compose.material.icons.filled.VolumeUp
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.unit.TextUnit
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.dictalearn.app.domain.dictionary.Dictionary
import com.dictalearn.app.domain.translation.SentenceTranslator
import com.dictalearn.app.ui.theme.Dicta
import kotlinx.coroutines.launch

/** Everything the word card needs, provided once near the root of the app. */
class WordTools(
    val dictionary: Dictionary?,
    val translator: SentenceTranslator?,
    val speak: (String) -> Unit,
    val addUnknown: (word: String, lessonId: String, segmentId: Int) -> Unit
)

val LocalWordTools = staticCompositionLocalOf<WordTools?> { null }

/**
 * A revealed sentence whose words open a bottom-sheet word card (Faz 7.1 / 7.4).
 * Only shown after the answer is submitted, so the copy-protection rule holds.
 */
@OptIn(ExperimentalLayoutApi::class, ExperimentalMaterial3Api::class)
@Composable
fun WordLookupSentence(
    text: String,
    lessonId: String,
    segmentId: Int,
    fontSize: TextUnit,
    lineHeight: TextUnit
) {
    val tools = LocalWordTools.current
    val words = remember(text) { text.split(Regex("\\s+")).filter { it.isNotBlank() } }
    var selected by remember(text) { mutableStateOf<Int?>(null) }

    FlowRow(horizontalArrangement = Arrangement.spacedBy(6.dp), verticalArrangement = Arrangement.spacedBy(2.dp)) {
        words.forEachIndexed { i, w ->
            Text(
                w,
                fontFamily = FontFamily.Serif,
                fontSize = fontSize,
                lineHeight = lineHeight,
                color = if (selected == i) Dicta.Accent else Dicta.TextPrimary,
                modifier = Modifier
                    .clip(RoundedCornerShape(4.dp))
                    .clickable(enabled = tools != null && Dictionary.normalize(w).isNotEmpty()) { selected = i }
            )
        }
    }

    val index = selected
    if (tools != null && index != null) {
        val entry = remember(index, tools.dictionary) { tools.dictionary?.lookupInSentence(words, index) }
        val headword = entry?.headword ?: Dictionary.normalize(words[index])
        var saved by remember(headword) { mutableStateOf(false) }
        var translation by remember(index) { mutableStateOf<String?>(null) }
        var translating by remember(index) { mutableStateOf(false) }
        val scope = rememberCoroutineScope()

        ModalBottomSheet(onDismissRequest = { selected = null }, containerColor = Dicta.Surface) {
            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(start = 20.dp, end = 20.dp, bottom = 32.dp),
                verticalArrangement = Arrangement.spacedBy(10.dp)
            ) {
                Text(headword, fontFamily = FontFamily.Serif, fontSize = 26.sp, color = Dicta.TextPrimary)
                Text(
                    entry?.meaning ?: if (tools.dictionary == null) "Sözlük yükleniyor…" else "Çevrimdışı sözlükte bulunamadı.",
                    color = if (entry != null) Dicta.TextSecondary else Dicta.TextMuted,
                    fontSize = 15.sp
                )
                Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                    FilledTonalButton(onClick = { tools.speak(headword) }) {
                        Icon(Icons.Default.VolumeUp, contentDescription = null, modifier = Modifier.size(16.dp))
                        Spacer(Modifier.width(6.dp))
                        Text("Telaffuz")
                    }
                    FilledTonalButton(
                        onClick = {
                            tools.addUnknown(headword, lessonId, segmentId)
                            saved = true
                        },
                        enabled = !saved
                    ) {
                        Icon(if (saved) Icons.Default.Check else Icons.Default.BookmarkAdd, contentDescription = null, modifier = Modifier.size(16.dp))
                        Spacer(Modifier.width(6.dp))
                        Text(if (saved) "Defterde" else "Deftere ekle")
                    }
                }
                if (tools.translator != null) {
                    HorizontalDivider(color = Dicta.Outline)
                    TextButton(
                        onClick = {
                            translating = true
                            scope.launch {
                                translation = tools.translator.translate(text).fold(
                                    onSuccess = { it },
                                    onFailure = { "Çeviri yapılamadı. İlk kullanımda dil modelini indirmek için internet gerekir." }
                                )
                                translating = false
                            }
                        },
                        enabled = !translating
                    ) {
                        Icon(Icons.Default.Translate, contentDescription = null, modifier = Modifier.size(16.dp))
                        Spacer(Modifier.width(6.dp))
                        Text("Cümleyi cihazda çevir (ML Kit)")
                    }
                    if (translating) {
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            CircularProgressIndicator(modifier = Modifier.size(16.dp), strokeWidth = 2.dp, color = Dicta.Accent)
                            Spacer(Modifier.width(8.dp))
                            Text("Çevriliyor…", color = Dicta.TextMuted, fontSize = 13.sp)
                        }
                    }
                    translation?.let {
                        Text(
                            it,
                            color = Dicta.TextPrimary,
                            fontSize = 14.sp,
                            modifier = Modifier
                                .fillMaxWidth()
                                .clip(RoundedCornerShape(10.dp))
                                .background(Dicta.Accent.copy(alpha = 0.08f))
                                .padding(10.dp)
                        )
                    }
                }
            }
        }
    }
}
