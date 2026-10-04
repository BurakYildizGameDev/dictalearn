package com.dictalearn.app.ui

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.Check
import androidx.compose.material.icons.filled.ChevronLeft
import androidx.compose.material.icons.filled.ChevronRight
import androidx.compose.material.icons.filled.EmojiEvents
import androidx.compose.material.icons.filled.Lightbulb
import androidx.compose.material.icons.filled.Mic
import androidx.compose.material.icons.filled.Pause
import androidx.compose.material.icons.filled.Refresh
import androidx.compose.material.icons.filled.SkipNext
import androidx.compose.material.icons.filled.Visibility
import androidx.compose.material.icons.filled.VisibilityOff
import androidx.compose.material.icons.filled.VolumeUp
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.focus.FocusRequester
import androidx.compose.ui.focus.focusRequester
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardCapitalization
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.dictalearn.app.domain.audio.AudioStatus
import com.dictalearn.app.domain.words.WordFeedback
import com.dictalearn.app.ui.theme.Dicta
import kotlin.math.roundToInt

private val noAutoCorrect = KeyboardOptions(
    capitalization = KeyboardCapitalization.None,
    autoCorrect = false,
    keyboardType = KeyboardType.Text,
    imeAction = ImeAction.Done
)

@OptIn(ExperimentalMaterial3Api::class, ExperimentalLayoutApi::class)
@Composable
fun StudySessionScreen(
    viewModel: StudySessionViewModel,
    title: String = viewModel.lesson.title,
    audioStatus: AudioStatus = AudioStatus.IDLE,
    onPause: () -> Unit = {},
    onBack: (() -> Unit)? = null,
    modifier: Modifier = Modifier
) {
    val state by viewModel.state.collectAsState()
    val studyMode by viewModel.studyMode.collectAsState()
    val currentIndex by viewModel.currentSegmentIndex.collectAsState()
    val currentSpeed by viewModel.speed.collectAsState()
    val autoPlay by viewModel.autoPlay.collectAsState()

    val totalSegments = viewModel.totalSegments
    val progress = (currentIndex + (if (state == SessionState.COMPLETED) 1f else 0f)) / totalSegments
    val imeVisible = WindowInsets.isImeVisible

    val listen: () -> Unit = {
        if (audioStatus == AudioStatus.PLAYING) onPause() else viewModel.replaySegment()
    }

    Scaffold(
        modifier = modifier,
        containerColor = Dicta.Background,
        topBar = {
            Column {
                TopAppBar(
                    navigationIcon = {
                        if (onBack != null) {
                            IconButton(onClick = onBack) {
                                Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Kütüphane")
                            }
                        }
                    },
                    title = {
                        Column {
                            Text(
                                title,
                                fontFamily = FontFamily.Serif,
                                fontSize = 18.sp,
                                maxLines = 1,
                                overflow = TextOverflow.Ellipsis
                            )
                            Text(
                                "Cümle ${currentIndex + 1} / $totalSegments",
                                fontSize = 12.sp,
                                color = Dicta.TextMuted
                            )
                        }
                    },
                    actions = {
                        IconButton(onClick = { viewModel.previousSegment() }, enabled = currentIndex > 0) {
                            Icon(Icons.Default.ChevronLeft, contentDescription = "Önceki cümle")
                        }
                        IconButton(onClick = { viewModel.skipSegment() }, enabled = currentIndex < totalSegments - 1) {
                            Icon(Icons.Default.ChevronRight, contentDescription = "İleri atla")
                        }
                    },
                    colors = TopAppBarDefaults.topAppBarColors(containerColor = Dicta.Background)
                )
                LinearProgressIndicator(
                    progress = { progress },
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(2.dp),
                    color = Dicta.Accent,
                    trackColor = Dicta.Surface
                )
            }
        },
        bottomBar = {
            // Settings get out of the way while typing.
            if (!imeVisible && state != SessionState.COMPLETED) {
                SettingsBar(
                    studyMode = studyMode,
                    speed = currentSpeed,
                    autoPlay = autoPlay,
                    onMode = viewModel::setStudyMode,
                    onSpeed = viewModel::setSpeed,
                    onAutoPlay = { viewModel.setAutoPlay(!autoPlay) }
                )
            }
        }
    ) { padding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding)
                .consumeWindowInsets(padding)
                .imePadding()
                .verticalScroll(rememberScrollState())
                .padding(horizontal = 16.dp, vertical = 16.dp),
            verticalArrangement = Arrangement.spacedBy(14.dp)
        ) {
            when (state) {
                SessionState.DICTATING ->
                    if (studyMode == StudyMode.SENTENCE) {
                        SentenceDictation(viewModel, audioStatus, listen)
                    } else {
                        WordDictation(viewModel, audioStatus, listen)
                    }
                SessionState.REVIEWING -> Reviewing(viewModel, audioStatus, listen)
                SessionState.SHADOWING -> Shadowing(viewModel, audioStatus, listen)
                SessionState.COMPLETED -> Completed(viewModel, onBack)
            }
        }
    }
}

// ─── Building blocks ────────────────────────────────────────────────────────

@Composable
private fun StageCard(
    border: Color = Dicta.Outline,
    background: Color = Dicta.Surface.copy(alpha = 0.6f),
    content: @Composable ColumnScope.() -> Unit
) {
    Column(
        modifier = Modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(18.dp))
            .background(background)
            .border(1.dp, border, RoundedCornerShape(18.dp))
            .padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp),
        content = content
    )
}

@Composable
private fun Eyebrow(text: String, color: Color = Dicta.TextMuted) {
    Text(text.uppercase(), style = MaterialTheme.typography.labelSmall, color = color)
}

@Composable
private fun ListenButton(status: AudioStatus, label: String = "Dinle", onClick: () -> Unit) {
    val playing = status == AudioStatus.PLAYING
    FilledTonalButton(onClick = onClick, shape = RoundedCornerShape(12.dp)) {
        Icon(if (playing) Icons.Default.Pause else Icons.Default.VolumeUp, contentDescription = null, modifier = Modifier.size(18.dp))
        Spacer(Modifier.width(6.dp))
        Text(if (playing) "Duraklat" else label)
    }
}

@Composable
private fun studyFieldColors(accent: Color = Dicta.Accent, error: Boolean = false) = OutlinedTextFieldDefaults.colors(
    focusedTextColor = Dicta.TextPrimary,
    unfocusedTextColor = Dicta.TextPrimary,
    focusedContainerColor = Color.Black.copy(alpha = 0.3f),
    unfocusedContainerColor = Color.Black.copy(alpha = 0.3f),
    focusedBorderColor = if (error) Dicta.Error else accent,
    unfocusedBorderColor = if (error) Dicta.Error else Dicta.Outline
)

@Composable
private fun SegmentNote(text: String) {
    Text(
        text,
        color = Dicta.Warning.copy(alpha = 0.9f),
        fontSize = 12.sp,
        lineHeight = 17.sp,
        modifier = Modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(12.dp))
            .background(Dicta.Warning.copy(alpha = 0.06f))
            .padding(10.dp)
    )
}

@Composable
private fun SettingsBar(
    studyMode: StudyMode,
    speed: Float,
    autoPlay: Boolean,
    onMode: (StudyMode) -> Unit,
    onSpeed: (Float) -> Unit,
    onAutoPlay: () -> Unit
) {
    Surface(color = Dicta.Surface, tonalElevation = 0.dp) {
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .navigationBarsPadding()
                .horizontalScroll(rememberScrollState())
                .padding(horizontal = 12.dp, vertical = 8.dp),
            horizontalArrangement = Arrangement.spacedBy(6.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            FilterChip(selected = studyMode == StudyMode.SENTENCE, onClick = { onMode(StudyMode.SENTENCE) }, label = { Text("Cümle") })
            FilterChip(selected = studyMode == StudyMode.WORD, onClick = { onMode(StudyMode.WORD) }, label = { Text("Kelime") })
            VerticalDivider(modifier = Modifier.height(24.dp).padding(horizontal = 4.dp), color = Dicta.Outline)
            listOf(0.75f, 1.0f, 1.25f).forEach { s ->
                FilterChip(
                    selected = speed == s,
                    onClick = { onSpeed(s) },
                    label = { Text(if (s == 1.0f) "1x" else "${s}x") }
                )
            }
            VerticalDivider(modifier = Modifier.height(24.dp).padding(horizontal = 4.dp), color = Dicta.Outline)
            FilterChip(selected = autoPlay, onClick = onAutoPlay, label = { Text("Otomatik çal") })
        }
    }
}

// ─── Stages ─────────────────────────────────────────────────────────────────

@Composable
private fun SentenceDictation(viewModel: StudySessionViewModel, status: AudioStatus, listen: () -> Unit) {
    val typedText by viewModel.typedText.collectAsState()
    val replayCount by viewModel.replayCount.collectAsState()
    val focus = remember { FocusRequester() }
    LaunchedEffect(viewModel.currentSegmentIndex.collectAsState().value) { runCatching { focus.requestFocus() } }

    StageCard {
        Row(verticalAlignment = Alignment.CenterVertically) {
            ListenButton(status, onClick = listen)
            Spacer(Modifier.weight(1f))
            Text(
                if (replayCount > 0) "$replayCount kez dinlendi" else "Dinle, duyduğunu yaz",
                color = Dicta.TextMuted,
                fontSize = 12.sp
            )
        }
        OutlinedTextField(
            value = typedText,
            onValueChange = viewModel::setTypedText,
            modifier = Modifier
                .fillMaxWidth()
                .heightIn(min = 120.dp)
                .focusRequester(focus),
            textStyle = LocalTextStyle.current.copy(fontFamily = FontFamily.Serif, fontSize = 20.sp, lineHeight = 28.sp),
            placeholder = { Text("Duyduğun cümleyi buraya yaz…", color = Dicta.TextMuted) },
            keyboardOptions = noAutoCorrect,
            keyboardActions = KeyboardActions(onDone = { viewModel.submitAnswer() }),
            colors = studyFieldColors(),
            shape = RoundedCornerShape(14.dp)
        )
        Row(verticalAlignment = Alignment.CenterVertically) {
            TextButton(onClick = viewModel::giveUp) {
                Text("Bilmiyorum / Göster", color = Dicta.TextSecondary)
            }
            Spacer(Modifier.weight(1f))
            Button(onClick = viewModel::submitAnswer, enabled = typedText.isNotBlank(), shape = RoundedCornerShape(12.dp)) {
                Icon(Icons.Default.Check, contentDescription = null, modifier = Modifier.size(18.dp))
                Spacer(Modifier.width(6.dp))
                Text("Kontrol Et")
            }
        }
    }
}

@OptIn(ExperimentalLayoutApi::class)
@Composable
private fun WordDictation(viewModel: StudySessionViewModel, status: AudioStatus, listen: () -> Unit) {
    val targetWords by viewModel.targetWords.collectAsState()
    val currentWordIndex by viewModel.currentWordIndex.collectAsState()
    val typedWord by viewModel.typedWord.collectAsState()
    val wordFeedback by viewModel.wordFeedback.collectAsState()
    val autoSpeakWord by viewModel.autoSpeakWord.collectAsState()
    val currentWord = viewModel.currentWord
    val incorrect = wordFeedback == WordFeedback.INCORRECT
    val focus = remember { FocusRequester() }
    LaunchedEffect(currentWordIndex) { runCatching { focus.requestFocus() } }

    StageCard {
        Row(verticalAlignment = Alignment.CenterVertically) {
            Text(
                "Kelime ${currentWordIndex + 1} / ${targetWords.size}",
                color = Dicta.TextSecondary,
                fontSize = 12.sp
            )
            Spacer(Modifier.weight(1f))
            FilterChip(
                selected = autoSpeakWord,
                onClick = viewModel::toggleAutoSpeakWord,
                label = { Text(if (autoSpeakWord) "Oto-oku açık" else "Oto-oku kapalı", fontSize = 11.sp) }
            )
        }
        ListenButton(status, label = "Cümleyi dinle", onClick = listen)

        // Future words are masked: only solved words are shown.
        FlowRow(horizontalArrangement = Arrangement.spacedBy(8.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
            targetWords.forEachIndexed { idx, token ->
                when {
                    idx < currentWordIndex -> Text(
                        token.raw,
                        color = Dicta.Success,
                        fontFamily = FontFamily.Serif,
                        fontSize = 17.sp,
                        modifier = Modifier
                            .clip(RoundedCornerShape(8.dp))
                            .background(Dicta.Success.copy(alpha = 0.1f))
                            .clickable { viewModel.speakWord(token.clean) }
                            .padding(horizontal = 10.dp, vertical = 5.dp)
                    )
                    idx == currentWordIndex -> Text(
                        "[${idx + 1}. Kelime]${token.punctuation ?: ""}",
                        color = if (incorrect) Dicta.Error else Dicta.Accent,
                        fontWeight = FontWeight.SemiBold,
                        fontSize = 14.sp,
                        modifier = Modifier
                            .border(2.dp, if (incorrect) Dicta.Error else Dicta.Accent, RoundedCornerShape(8.dp))
                            .padding(horizontal = 10.dp, vertical = 5.dp)
                    )
                    else -> Text(
                        "••••",
                        color = Color(0xFF3F3F46),
                        fontSize = 14.sp,
                        modifier = Modifier
                            .clip(RoundedCornerShape(8.dp))
                            .background(Color.White.copy(alpha = 0.04f))
                            .padding(horizontal = 10.dp, vertical = 5.dp)
                    )
                }
            }
        }

        OutlinedTextField(
            value = typedWord,
            onValueChange = { value ->
                // Space submits the word, like on the web.
                if (value.endsWith(" ") && value.isNotBlank()) {
                    viewModel.setTypedWord(value.trim())
                    viewModel.submitWord()
                } else {
                    viewModel.setTypedWord(value)
                }
            },
            modifier = Modifier
                .fillMaxWidth()
                .focusRequester(focus),
            singleLine = true,
            textStyle = LocalTextStyle.current.copy(fontFamily = FontFamily.Serif, fontSize = 22.sp),
            placeholder = { Text("${currentWordIndex + 1}. kelimeyi yaz…", color = Dicta.TextMuted) },
            keyboardOptions = noAutoCorrect,
            keyboardActions = KeyboardActions(onDone = { viewModel.submitWord() }),
            colors = studyFieldColors(error = incorrect),
            shape = RoundedCornerShape(14.dp)
        )
        if (incorrect && currentWord != null) {
            Text(
                "Yanlış, tekrar dene. İpucu: “${currentWord.clean.take(1).uppercase()}” ile başlıyor, ${currentWord.clean.length} harf.",
                color = Dicta.Error,
                fontSize = 12.sp
            )
        }
        Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
            Button(
                onClick = viewModel::submitWord,
                enabled = typedWord.isNotBlank(),
                shape = RoundedCornerShape(12.dp),
                modifier = Modifier
                    .weight(1f)
                    .height(48.dp)
            ) { Text("Kontrol") }
            OutlinedButton(
                onClick = viewModel::giveLetterHint,
                shape = RoundedCornerShape(12.dp),
                border = BorderStroke(1.dp, Dicta.Outline),
                modifier = Modifier
                    .weight(1f)
                    .height(48.dp)
            ) {
                Icon(Icons.Default.Lightbulb, contentDescription = null, tint = Dicta.Warning, modifier = Modifier.size(16.dp))
                Spacer(Modifier.width(4.dp))
                Text("İpucu", color = Dicta.TextPrimary)
            }
            OutlinedButton(
                onClick = viewModel::speakCurrentWord,
                shape = RoundedCornerShape(12.dp),
                border = BorderStroke(1.dp, Dicta.Outline),
                modifier = Modifier
                    .weight(1f)
                    .height(48.dp)
            ) {
                Icon(Icons.Default.VolumeUp, contentDescription = null, modifier = Modifier.size(16.dp))
                Spacer(Modifier.width(4.dp))
                Text("Oku", color = Dicta.TextPrimary)
            }
        }
        Row {
            TextButton(onClick = viewModel::skipWord) {
                Icon(Icons.Default.SkipNext, contentDescription = null, modifier = Modifier.size(16.dp), tint = Dicta.TextSecondary)
                Spacer(Modifier.width(4.dp))
                Text("Kelimeyi atla", color = Dicta.TextSecondary)
            }
            Spacer(Modifier.weight(1f))
            TextButton(onClick = viewModel::giveUp) {
                Text("Tüm cümleyi göster", color = Dicta.TextMuted)
            }
        }
    }
}

@Composable
private fun Reviewing(viewModel: StudySessionViewModel, status: AudioStatus, listen: () -> Unit) {
    val diffResult by viewModel.diffResult.collectAsState()
    val correctionText by viewModel.correctionText.collectAsState()
    val correctionDiff by viewModel.correctionDiff.collectAsState()
    val segment = viewModel.currentSegment

    diffResult?.let { DiffViewCompose(diff = it) }

    StageCard {
        Row(verticalAlignment = Alignment.CenterVertically) {
            Eyebrow("Orijinal")
            Spacer(Modifier.weight(1f))
            ListenButton(status, onClick = listen)
        }
        Text(segment.text, fontFamily = FontFamily.Serif, fontSize = 21.sp, lineHeight = 30.sp, color = Dicta.TextPrimary)
        segment.translation?.let { Text(it, color = Dicta.TextSecondary, fontSize = 14.sp, lineHeight = 20.sp) }
        segment.notes?.let { SegmentNote(it) }
    }

    StageCard(border = Dicta.Warning.copy(alpha = 0.25f), background = Dicta.Warning.copy(alpha = 0.03f)) {
        Row(verticalAlignment = Alignment.CenterVertically) {
            Icon(Icons.Default.Refresh, contentDescription = null, tint = Dicta.Warning, modifier = Modifier.size(16.dp))
            Spacer(Modifier.width(6.dp))
            Text("Cümleyi düzelterek yeniden yaz", color = Dicta.Warning, fontWeight = FontWeight.Medium, fontSize = 14.sp)
        }
        OutlinedTextField(
            value = correctionText,
            onValueChange = viewModel::setCorrectionText,
            modifier = Modifier.fillMaxWidth(),
            textStyle = LocalTextStyle.current.copy(fontFamily = FontFamily.Serif, fontSize = 18.sp),
            placeholder = { Text("Doğru halini yaz…", color = Dicta.TextMuted) },
            keyboardOptions = noAutoCorrect,
            keyboardActions = KeyboardActions(onDone = { viewModel.submitCorrection() }),
            colors = studyFieldColors(accent = Dicta.Warning),
            shape = RoundedCornerShape(14.dp)
        )
        correctionDiff?.let { cDiff ->
            if (!cDiff.isPerfect) {
                Text("Hâlâ eksik ya da yanlış kelimeler var:", color = Dicta.Error, fontSize = 12.sp)
                DiffViewCompose(diff = cDiff)
            }
        }
        Row(verticalAlignment = Alignment.CenterVertically) {
            TextButton(onClick = viewModel::skipCorrection) { Text("Düzeltmeyi atla", color = Dicta.TextSecondary) }
            Spacer(Modifier.weight(1f))
            Button(
                onClick = viewModel::submitCorrection,
                enabled = correctionText.isNotBlank(),
                colors = ButtonDefaults.buttonColors(containerColor = Dicta.Warning, contentColor = Color(0xFF451A03)),
                shape = RoundedCornerShape(12.dp)
            ) { Text("Kontrol Et") }
        }
    }
}

@Composable
private fun Shadowing(viewModel: StudySessionViewModel, status: AudioStatus, listen: () -> Unit) {
    val diffResult by viewModel.diffResult.collectAsState()
    val showTranslation by viewModel.showTranslation.collectAsState()
    val currentIndex by viewModel.currentSegmentIndex.collectAsState()
    val segment = viewModel.currentSegment

    diffResult?.let { DiffViewCompose(diff = it) }

    StageCard(border = Dicta.Accent.copy(alpha = 0.25f), background = Dicta.Accent.copy(alpha = 0.04f)) {
        Row(verticalAlignment = Alignment.CenterVertically) {
            Icon(Icons.Default.Mic, contentDescription = null, tint = Dicta.Accent, modifier = Modifier.size(14.dp))
            Spacer(Modifier.width(6.dp))
            Eyebrow("Shadowing / Sesli tekrar", Dicta.Accent)
            Spacer(Modifier.weight(1f))
            TextButton(onClick = viewModel::toggleTranslation) {
                Icon(
                    if (showTranslation) Icons.Default.VisibilityOff else Icons.Default.Visibility,
                    contentDescription = null,
                    modifier = Modifier.size(16.dp)
                )
                Spacer(Modifier.width(4.dp))
                Text(if (showTranslation) "Çeviriyi gizle" else "Çeviriyi göster", fontSize = 12.sp)
            }
        }
        Text(segment.text, fontFamily = FontFamily.Serif, fontSize = 24.sp, lineHeight = 34.sp, color = Dicta.TextPrimary)
        if (showTranslation && segment.translation != null) {
            Text(segment.translation, color = Color(0xFFC7D2FE), fontSize = 15.sp, lineHeight = 22.sp)
        }
        segment.notes?.let { SegmentNote(it) }
        HorizontalDivider(color = Dicta.Outline)
        Row(verticalAlignment = Alignment.CenterVertically) {
            ListenButton(status, onClick = listen)
            Spacer(Modifier.width(12.dp))
            Text("Dinle ve konuşmacıyı taklit ederek yüksek sesle tekrar et.", color = Dicta.TextSecondary, fontSize = 12.sp)
        }
    }

    Button(
        onClick = viewModel::nextSegment,
        modifier = Modifier
            .fillMaxWidth()
            .height(52.dp),
        shape = RoundedCornerShape(14.dp)
    ) {
        Text(if (currentIndex >= viewModel.totalSegments - 1) "Dersi bitir" else "Sonraki cümle", fontSize = 15.sp)
        Spacer(Modifier.width(6.dp))
        Icon(Icons.Default.ChevronRight, contentDescription = null)
    }
}

@OptIn(ExperimentalLayoutApi::class)
@Composable
private fun Completed(viewModel: StudySessionViewModel, onBack: (() -> Unit)?) {
    val records = viewModel.records
    val avgAccuracy = if (records.isNotEmpty()) (records.map { it.accuracy }.average() * 100).roundToInt() else 0
    val perfectCount = records.count { it.isPerfect }
    val totalReplays = records.sumOf { it.replayCount }
    val lessonMistakes = remember(records.size) {
        viewModel.mistakeRepository?.getMistakes()
            ?.filter { it.lessonId == viewModel.lesson.lessonId }
            ?.groupingBy { it.word.lowercase() }?.eachCount()
            ?.entries?.sortedByDescending { it.value }?.take(12)
            ?: emptyList()
    }

    Column(
        modifier = Modifier
            .fillMaxWidth()
            .padding(vertical = 16.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        Box(
            modifier = Modifier
                .size(56.dp)
                .clip(RoundedCornerShape(16.dp))
                .background(Dicta.Warning.copy(alpha = 0.1f)),
            contentAlignment = Alignment.Center
        ) {
            Icon(Icons.Default.EmojiEvents, contentDescription = null, tint = Dicta.Warning)
        }
        Text("Ders tamamlandı", style = MaterialTheme.typography.headlineSmall)

        Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
            listOf(
                Triple("Doğruluk", "%$avgAccuracy", Dicta.Success),
                Triple("Kusursuz", "$perfectCount / ${records.size}", Dicta.TextPrimary),
                Triple("Tekrar", "$totalReplays", Dicta.TextPrimary)
            ).forEach { (label, value, color) ->
                Column(
                    modifier = Modifier
                        .weight(1f)
                        .clip(RoundedCornerShape(14.dp))
                        .background(Dicta.Surface)
                        .padding(12.dp),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Text(label, color = Dicta.TextMuted, fontSize = 11.sp)
                    Text(value, color = color, fontSize = 20.sp, fontWeight = FontWeight.SemiBold)
                }
            }
        }

        if (lessonMistakes.isNotEmpty()) {
            StageCard {
                Eyebrow("Hata defteri · tekrar et")
                FlowRow(horizontalArrangement = Arrangement.spacedBy(8.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
                    lessonMistakes.forEach { (word, count) ->
                        Text(
                            "$word ×$count",
                            color = Dicta.Error,
                            fontSize = 13.sp,
                            modifier = Modifier
                                .clip(RoundedCornerShape(8.dp))
                                .background(Dicta.Error.copy(alpha = 0.1f))
                                .padding(horizontal = 10.dp, vertical = 5.dp)
                        )
                    }
                }
            }
        }

        Button(onClick = viewModel::restart, shape = RoundedCornerShape(14.dp), modifier = Modifier.fillMaxWidth().height(50.dp)) {
            Text("Dersi tekrar başlat")
        }
        if (onBack != null) {
            OutlinedButton(onClick = onBack, shape = RoundedCornerShape(14.dp), modifier = Modifier.fillMaxWidth().height(50.dp)) {
                Text("Kütüphaneye dön", color = Dicta.TextPrimary)
            }
        }
    }
}
