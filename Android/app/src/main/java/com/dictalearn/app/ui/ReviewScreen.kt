package com.dictalearn.app.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.Check
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.EmojiEvents
import androidx.compose.material.icons.filled.VolumeUp
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.focus.FocusRequester
import androidx.compose.ui.focus.focusRequester
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardCapitalization
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.dictalearn.app.domain.dictionary.Dictionary
import com.dictalearn.app.domain.review.SrsCard
import com.dictalearn.app.domain.review.SrsStore
import com.dictalearn.app.domain.words.WordModeEngine
import com.dictalearn.app.ui.theme.Dicta

/**
 * Spaced-repetition review: hear the word, see its Turkish meaning, type it. The first answer of a
 * card moves it between Leitner boxes; missed cards come back once more at the end for practice.
 */
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ReviewScreen(
    srs: SrsStore,
    dictionary: Dictionary?,
    onSpeak: (String) -> Unit,
    onBack: () -> Unit
) {
    val queue = remember { mutableStateListOf<SrsCard>().apply { addAll(srs.dueCards()) } }
    val total = remember { queue.size }
    var position by remember { mutableIntStateOf(0) }
    var typed by remember { mutableStateOf("") }
    var feedback by remember { mutableStateOf<Boolean?>(null) }
    val results = remember { mutableStateMapOf<String, Boolean>() }
    val focus = remember { FocusRequester() }
    val card = queue.getOrNull(position)

    LaunchedEffect(card, position) {
        if (card != null) {
            onSpeak(card.word)
            runCatching { focus.requestFocus() }
        }
    }

    fun submit(gaveUp: Boolean = false) {
        val c = card ?: return
        if (feedback != null || (!gaveUp && typed.isBlank())) return
        val correct = !gaveUp && WordModeEngine.checkWord(c.word, typed)
        feedback = correct
        if (c.word !in results) {
            srs.answer(c.word, correct)
            results[c.word] = correct
            if (!correct) queue.add(c)
        }
        if (!correct) onSpeak(c.word)
    }

    fun next() {
        feedback = null
        typed = ""
        position++
    }

    Scaffold(
        containerColor = Dicta.Background,
        topBar = {
            TopAppBar(
                navigationIcon = {
                    IconButton(onClick = onBack) { Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Geri") }
                },
                title = {
                    Column {
                        Text("Kelime tekrarı", fontFamily = FontFamily.Serif)
                        if (total > 0) Text("${minOf(results.size + if (feedback == null) 1 else 0, total)} / $total", fontSize = 12.sp, color = Dicta.TextMuted)
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(containerColor = Dicta.Background)
            )
        }
    ) { padding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding)
                .imePadding()
                .padding(20.dp),
            verticalArrangement = Arrangement.spacedBy(14.dp)
        ) {
            when {
                total == 0 -> {
                    Text("Bugün tekrar edilecek kelime yok", fontFamily = FontFamily.Serif, fontSize = 22.sp, color = Dicta.TextPrimary)
                    Text("Yeni kelimeler dikte yaptıkça defterine eklenir.", color = Dicta.TextSecondary)
                    Button(onClick = onBack) { Text("Defterime dön") }
                }
                card == null -> {
                    val correct = results.values.count { it }
                    Icon(Icons.Default.EmojiEvents, contentDescription = null, tint = Dicta.Warning, modifier = Modifier.size(40.dp))
                    Text("Tekrar tamamlandı", fontFamily = FontFamily.Serif, fontSize = 26.sp, color = Dicta.TextPrimary)
                    Text(
                        "$total kelimenin $correct tanesini ilk denemede bildin. Bildiklerin daha seyrek, bilemediklerin yarın tekrar sorulacak.",
                        color = Dicta.TextSecondary
                    )
                    Button(onClick = onBack, modifier = Modifier.fillMaxWidth()) { Text("Defterime dön") }
                }
                else -> {
                    LinearProgressIndicator(
                        progress = { results.size.toFloat() / total },
                        modifier = Modifier.fillMaxWidth(),
                        color = Dicta.Accent,
                        trackColor = Dicta.Surface
                    )
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        FilledTonalButton(onClick = { onSpeak(card.word) }) {
                            Icon(Icons.Default.VolumeUp, contentDescription = null, modifier = Modifier.size(18.dp))
                            Spacer(Modifier.width(6.dp))
                            Text("Dinle")
                        }
                        Spacer(Modifier.weight(1f))
                        Text(
                            if (position >= total) "ek tekrar" else "Kutu ${card.box + 1} / 6",
                            color = Dicta.TextMuted,
                            fontSize = 12.sp
                        )
                    }
                    Text("Türkçesi:", color = Dicta.TextSecondary, fontSize = 13.sp)
                    Text(
                        dictionary?.lookup(card.word)?.meaning
                            ?: (card.word.take(1).uppercase() + "·".repeat((card.word.length - 1).coerceAtLeast(0))),
                        fontFamily = FontFamily.Serif,
                        fontSize = 24.sp,
                        color = Dicta.TextPrimary
                    )
                    OutlinedTextField(
                        value = typed,
                        onValueChange = { if (feedback == null) typed = it },
                        modifier = Modifier
                            .fillMaxWidth()
                            .focusRequester(focus),
                        singleLine = true,
                        textStyle = LocalTextStyle.current.copy(fontFamily = FontFamily.Serif, fontSize = 22.sp),
                        placeholder = { Text("Duyduğun kelimeyi yaz…", color = Dicta.TextMuted) },
                        keyboardOptions = KeyboardOptions(
                            capitalization = KeyboardCapitalization.None,
                            autoCorrect = false,
                            imeAction = ImeAction.Done
                        ),
                        keyboardActions = KeyboardActions(onDone = { if (feedback == null) submit() else next() }),
                        shape = RoundedCornerShape(14.dp)
                    )
                    feedback?.let { correct ->
                        Row(
                            modifier = Modifier
                                .fillMaxWidth()
                                .clip(RoundedCornerShape(12.dp))
                                .background((if (correct) Dicta.Success else Dicta.Error).copy(alpha = 0.1f))
                                .padding(12.dp),
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Icon(
                                if (correct) Icons.Default.Check else Icons.Default.Close,
                                contentDescription = null,
                                tint = if (correct) Dicta.Success else Dicta.Error
                            )
                            Spacer(Modifier.width(8.dp))
                            Text(if (correct) "Doğru! " else "Doğrusu: ", color = if (correct) Dicta.Success else Dicta.Error)
                            Text(card.word, fontFamily = FontFamily.Serif, fontSize = 18.sp, color = Dicta.TextPrimary)
                        }
                    }
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        if (feedback == null) {
                            TextButton(onClick = { submit(gaveUp = true) }) { Text("Bilmiyorum", color = Dicta.TextSecondary) }
                            Spacer(Modifier.weight(1f))
                            Button(onClick = { submit() }, enabled = typed.isNotBlank()) { Text("Kontrol Et") }
                        } else {
                            Spacer(Modifier.weight(1f))
                            Button(onClick = { next() }) { Text("Devam") }
                        }
                    }
                }
            }
        }
    }
}
