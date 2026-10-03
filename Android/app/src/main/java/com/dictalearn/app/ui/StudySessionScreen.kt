package com.dictalearn.app.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowForward
import androidx.compose.material.icons.filled.Check
import androidx.compose.material.icons.filled.HelpOutline
import androidx.compose.material.icons.filled.Refresh
import androidx.compose.material.icons.filled.Visibility
import androidx.compose.material.icons.filled.VisibilityOff
import androidx.compose.material.icons.filled.VolumeUp
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardCapitalization
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlin.math.roundToInt

@OptIn(ExperimentalMaterial3Api::class, ExperimentalLayoutApi::class)
@Composable
fun StudySessionScreen(
    viewModel: StudySessionViewModel,
    modifier: Modifier = Modifier
) {
    val state by viewModel.state.collectAsState()
    val currentIndex by viewModel.currentSegmentIndex.collectAsState()
    val typedText by viewModel.typedText.collectAsState()
    val correctionText by viewModel.correctionText.collectAsState()
    val diffResult by viewModel.diffResult.collectAsState()
    val correctionDiff by viewModel.correctionDiff.collectAsState()
    val replayCount by viewModel.replayCount.collectAsState()
    val showTranslation by viewModel.showTranslation.collectAsState()
    val currentSpeed by viewModel.speed.collectAsState()

    val currentSegment = viewModel.currentSegment
    val totalSegments = viewModel.totalSegments
    val progress = (currentIndex + (if (state == SessionState.COMPLETED) 1f else 0f)) / totalSegments

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Column {
                        Text(
                            text = viewModel.lesson.title,
                            fontSize = 16.sp,
                            fontWeight = FontWeight.Bold,
                            color = Color(0xFFF8FAFC)
                        )
                        Text(
                            text = "Cümle ${currentIndex + 1} / $totalSegments",
                            fontSize = 12.sp,
                            color = Color(0xFF94A3B8)
                        )
                    }
                },
                actions = {
                    // Speed selectors (F3.5)
                    listOf(0.75f, 1.0f, 1.25f).forEach { s ->
                        FilterChip(
                            selected = currentSpeed == s,
                            onClick = { viewModel.setSpeed(s) },
                            label = { Text("${s}x", fontSize = 11.sp) },
                            modifier = Modifier.padding(horizontal = 2.dp)
                        )
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(
                    containerColor = Color(0xFF0F172A)
                )
            )
        },
        containerColor = Color(0xFF020617)
    ) { padding ->
        Column(
            modifier = modifier
                .fillMaxSize()
                .padding(padding)
                .padding(horizontal = 16.dp, vertical = 12.dp)
                .verticalScroll(rememberScrollState()),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            // Linear Progress Bar
            LinearProgressIndicator(
                progress = { progress },
                modifier = Modifier
                    .fillMaxWidth()
                    .height(6.dp),
                color = Color(0xFF6366F1),
                trackColor = Color(0xFF1E293B)
            )

            // Audio Replay Bar & State Badge
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .background(Color(0xFF0F172A), RoundedCornerShape(12.dp))
                    .border(1.dp, Color(0xFF1E293B), RoundedCornerShape(12.dp))
                    .padding(12.dp),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Button(
                    onClick = { viewModel.replaySegment() },
                    colors = ButtonDefaults.buttonColors(containerColor = Color(0xFF4F46E5)),
                    shape = RoundedCornerShape(8.dp)
                ) {
                    Icon(Icons.Default.VolumeUp, contentDescription = "Dinle", modifier = Modifier.size(18.dp))
                    Spacer(modifier = Modifier.width(6.dp))
                    Text("Tekrar Dinle", fontSize = 13.sp)
                }

                Column(horizontalAlignment = Alignment.End) {
                    val stateLabel = when (state) {
                        SessionState.DICTATING -> "Dikte Modu"
                        SessionState.REVIEWING -> "Düzeltme Modu"
                        SessionState.SHADOWING -> "Shadowing Modu"
                        SessionState.COMPLETED -> "Tamamlandı"
                    }
                    val stateColor = when (state) {
                        SessionState.DICTATING -> Color(0xFF10B981)
                        SessionState.REVIEWING -> Color(0xFFF59E0B)
                        SessionState.SHADOWING -> Color(0xFF6366F1)
                        SessionState.COMPLETED -> Color(0xFF38BDF8)
                    }

                    Text(
                        text = stateLabel,
                        color = stateColor,
                        fontSize = 12.sp,
                        fontWeight = FontWeight.SemiBold
                    )
                    if (replayCount > 0) {
                        Text(
                            text = "($replayCount kez dinlendi)",
                            color = Color(0xFF94A3B8),
                            fontSize = 11.sp
                        )
                    }
                }
            }

            // MAIN AREA ACCORDING TO STATE
            when (state) {
                SessionState.DICTATING -> {
                    // DICTATING STATE: No original text in composition tree!
                    Text(
                        text = "Duyduğunuz cümleyi yazın:",
                        color = Color(0xFFCBD5E1),
                        fontSize = 14.sp,
                        fontWeight = FontWeight.Medium
                    )

                    OutlinedTextField(
                        value = typedText,
                        onValueChange = { viewModel.setTypedText(it) },
                        modifier = Modifier
                            .fillMaxWidth()
                            .heightIn(min = 120.dp),
                        placeholder = {
                            Text("Duyduğunuz cümleyi buraya yazın...", color = Color(0xFF64748B))
                        },
                        keyboardOptions = KeyboardOptions(
                            capitalization = KeyboardCapitalization.None,
                            autoCorrect = false,
                            keyboardType = KeyboardType.Text,
                            imeAction = ImeAction.Done
                        ),
                        keyboardActions = KeyboardActions(
                            onDone = { viewModel.submitAnswer() }
                        ),
                        colors = OutlinedTextFieldDefaults.colors(
                            focusedTextColor = Color(0xFFF8FAFC),
                            unfocusedTextColor = Color(0xFFF8FAFC),
                            focusedContainerColor = Color(0xFF0F172A),
                            unfocusedContainerColor = Color(0xFF0F172A),
                            focusedBorderColor = Color(0xFF6366F1),
                            unfocusedBorderColor = Color(0xFF334155)
                        ),
                        shape = RoundedCornerShape(12.dp)
                    )

                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        TextButton(
                            onClick = { viewModel.giveUp() }
                        ) {
                            Icon(Icons.Default.HelpOutline, contentDescription = null, tint = Color(0xFFFBBF24), modifier = Modifier.size(16.dp))
                            Spacer(modifier = Modifier.width(4.dp))
                            Text("Cevabı Göster", color = Color(0xFFFBBF24), fontSize = 13.sp)
                        }

                        Button(
                            onClick = { viewModel.submitAnswer() },
                            enabled = typedText.isNotBlank(),
                            colors = ButtonDefaults.buttonColors(containerColor = Color(0xFF059669)),
                            shape = RoundedCornerShape(8.dp)
                        ) {
                            Icon(Icons.Default.Check, contentDescription = null, modifier = Modifier.size(18.dp))
                            Spacer(modifier = Modifier.width(4.dp))
                            Text("Kontrol Et", fontSize = 13.sp)
                        }
                    }
                }

                SessionState.REVIEWING -> {
                    // Diff Result
                    diffResult?.let { diff ->
                        DiffViewCompose(diff = diff)
                    }

                    // Original text & translation card
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .background(Color(0xFF0F172A), RoundedCornerShape(12.dp))
                            .border(1.dp, Color(0xFF334155), RoundedCornerShape(12.dp))
                            .padding(16.dp),
                        verticalArrangement = Arrangement.spacedBy(10.dp)
                    ) {
                        Text(
                            text = "ORİJİNAL METİN:",
                            color = Color(0xFF94A3B8),
                            fontSize = 11.sp,
                            fontWeight = FontWeight.Bold
                        )
                        Text(
                            text = currentSegment.text,
                            color = Color(0xFFF8FAFC),
                            fontSize = 17.sp,
                            fontWeight = FontWeight.SemiBold
                        )

                        currentSegment.translation?.let { tr ->
                            HorizontalDivider(color = Color(0xFF1E293B))
                            Text(
                                text = "ÇEVİRİ:",
                                color = Color(0xFF94A3B8),
                                fontSize = 11.sp,
                                fontWeight = FontWeight.Bold
                            )
                            Text(
                                text = tr,
                                color = Color(0xFFCBD5E1),
                                fontSize = 15.sp
                            )
                        }

                        currentSegment.notes?.let { note ->
                            HorizontalDivider(color = Color(0xFF1E293B))
                            Text(
                                text = "NOT: $note",
                                color = Color(0xFFFDE047),
                                fontSize = 13.sp
                            )
                        }
                    }

                    // Correction Card (F3.1)
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .background(Color(0xFF0F172A), RoundedCornerShape(12.dp))
                            .border(1.dp, Color(0xFFF59E0B).copy(alpha = 0.4f), RoundedCornerShape(12.dp))
                            .padding(16.dp),
                        verticalArrangement = Arrangement.spacedBy(12.dp)
                    ) {
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.spacedBy(6.dp)
                        ) {
                            Icon(Icons.Default.Refresh, contentDescription = null, tint = Color(0xFFFBBF24), modifier = Modifier.size(16.dp))
                            Text(
                                text = "Cümleyi düzelterek yeniden yazın:",
                                color = Color(0xFFFBBF24),
                                fontSize = 13.sp,
                                fontWeight = FontWeight.SemiBold
                            )
                        }

                        OutlinedTextField(
                            value = correctionText,
                            onValueChange = { viewModel.setCorrectionText(it) },
                            modifier = Modifier.fillMaxWidth(),
                            placeholder = {
                                Text("Doğru halini yazın...", color = Color(0xFF64748B), fontSize = 14.sp)
                            },
                            keyboardOptions = KeyboardOptions(
                                capitalization = KeyboardCapitalization.None,
                                autoCorrect = false,
                                keyboardType = KeyboardType.Text,
                                imeAction = ImeAction.Done
                            ),
                            keyboardActions = KeyboardActions(
                                onDone = { viewModel.submitCorrection() }
                            ),
                            colors = OutlinedTextFieldDefaults.colors(
                                focusedTextColor = Color(0xFFF8FAFC),
                                unfocusedTextColor = Color(0xFFF8FAFC),
                                focusedContainerColor = Color(0xFF020617),
                                unfocusedContainerColor = Color(0xFF020617),
                                focusedBorderColor = Color(0xFFF59E0B),
                                unfocusedBorderColor = Color(0xFF334155)
                            ),
                            shape = RoundedCornerShape(8.dp)
                        )

                        // Real-time correction diff feedback
                        correctionDiff?.let { cDiff ->
                            if (!cDiff.isPerfect) {
                                Text(
                                    text = "Düzeltmenizde hala eksik veya yanlış kelimeler var:",
                                    color = Color(0xFFF87171),
                                    fontSize = 12.sp
                                )
                                DiffViewCompose(diff = cDiff)
                            }
                        }

                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            TextButton(onClick = { viewModel.skipCorrection() }) {
                                Text("Düzeltmeyi Atla", color = Color(0xFF94A3B8), fontSize = 12.sp)
                            }

                            Button(
                                onClick = { viewModel.submitCorrection() },
                                enabled = correctionText.isNotBlank(),
                                colors = ButtonDefaults.buttonColors(containerColor = Color(0xFFD97706)),
                                shape = RoundedCornerShape(8.dp)
                            ) {
                                Icon(Icons.Default.Check, contentDescription = null, modifier = Modifier.size(16.dp))
                                Spacer(modifier = Modifier.width(4.dp))
                                Text("Kontrol Et", fontSize = 12.sp)
                            }
                        }
                    }
                }

                SessionState.SHADOWING -> {
                    // Diff Result
                    diffResult?.let { diff ->
                        DiffViewCompose(diff = diff)
                    }

                    // Shadowing Card (F3.2)
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .background(Color(0xFF0F172A), RoundedCornerShape(12.dp))
                            .border(1.dp, Color(0xFF6366F1).copy(alpha = 0.5f), RoundedCornerShape(12.dp))
                            .padding(16.dp),
                        verticalArrangement = Arrangement.spacedBy(14.dp)
                    ) {
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Text(
                                text = "✨ SHADOWING / SESLİ TEKRAR",
                                color = Color(0xFF818CF8),
                                fontSize = 12.sp,
                                fontWeight = FontWeight.Bold
                            )

                            // Translation Toggle Button
                            FilledTonalButton(
                                onClick = { viewModel.toggleTranslation() },
                                shape = RoundedCornerShape(8.dp),
                                contentPadding = PaddingValues(horizontal = 10.dp, vertical = 6.dp)
                            ) {
                                Icon(
                                    imageVector = if (showTranslation) Icons.Default.VisibilityOff else Icons.Default.Visibility,
                                    contentDescription = null,
                                    modifier = Modifier.size(16.dp)
                                )
                                Spacer(modifier = Modifier.width(4.dp))
                                Text(
                                    text = if (showTranslation) "Çeviriyi Gizle" else "Çeviriyi Göster",
                                    fontSize = 11.sp
                                )
                            }
                        }

                        Text(
                            text = currentSegment.text,
                            color = Color(0xFFF8FAFC),
                            fontSize = 20.sp,
                            fontWeight = FontWeight.Bold,
                            lineHeight = 28.sp
                        )

                        // Listen & repeat callout
                        Row(
                            modifier = Modifier
                                .fillMaxWidth()
                                .background(Color(0xFF020617), RoundedCornerShape(8.dp))
                                .border(1.dp, Color(0xFF1E293B), RoundedCornerShape(8.dp))
                                .padding(10.dp),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Text(
                                text = "Dinleyin ve konuşmacıyı taklit ederek sesli tekrar edin.",
                                color = Color(0xFF94A3B8),
                                fontSize = 12.sp,
                                modifier = Modifier.weight(1f)
                            )
                            Spacer(modifier = Modifier.width(8.dp))
                            Button(
                                onClick = { viewModel.replaySegment() },
                                colors = ButtonDefaults.buttonColors(containerColor = Color(0xFF4F46E5)),
                                shape = RoundedCornerShape(6.dp),
                                contentPadding = PaddingValues(horizontal = 10.dp, vertical = 6.dp)
                            ) {
                                Icon(Icons.Default.VolumeUp, contentDescription = null, modifier = Modifier.size(14.dp))
                                Spacer(modifier = Modifier.width(4.dp))
                                Text("Dinle", fontSize = 12.sp)
                            }
                        }

                        // Translation (toggleable)
                        if (showTranslation && currentSegment.translation != null) {
                            Column(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .background(Color(0xFF1E1B4B).copy(alpha = 0.5f), RoundedCornerShape(8.dp))
                                    .padding(10.dp)
                            ) {
                                Text(
                                    text = "TÜRKÇE ÇEVİRİ:",
                                    color = Color(0xFFA5B4FC),
                                    fontSize = 10.sp,
                                    fontWeight = FontWeight.Bold
                                )
                                Spacer(modifier = Modifier.height(2.dp))
                                Text(
                                    text = currentSegment.translation,
                                    color = Color(0xFFE0E7FF),
                                    fontSize = 14.sp
                                )
                            }
                        }

                        currentSegment.notes?.let { note ->
                            Text(
                                text = "Not: $note",
                                color = Color(0xFFFDE047),
                                fontSize = 12.sp
                            )
                        }
                    }

                    // Next Segment Button
                    Button(
                        onClick = { viewModel.nextSegment() },
                        modifier = Modifier.align(Alignment.End),
                        colors = ButtonDefaults.buttonColors(containerColor = Color(0xFF4F46E5)),
                        shape = RoundedCornerShape(8.dp)
                    ) {
                        Text(
                            text = if (currentIndex >= totalSegments - 1) "Dersi Bitir" else "Sonraki Cümle",
                            fontSize = 14.sp
                        )
                        Spacer(modifier = Modifier.width(6.dp))
                        Icon(Icons.Default.ArrowForward, contentDescription = null, modifier = Modifier.size(16.dp))
                    }
                }

                SessionState.COMPLETED -> {
                    val records = viewModel.records
                    val avgAccuracy = if (records.isNotEmpty()) {
                        (records.map { it.accuracy }.average() * 100).roundToInt()
                    } else 100
                    val perfectCount = records.count { it.isPerfect }
                    val totalReplays = records.sumOf { it.replayCount }
                    val mistakeFrequencies = viewModel.mistakeRepository?.getWordFrequencies() ?: emptyMap()
                    val topMistakes = mistakeFrequencies.entries.sortedByDescending { it.value }.take(10)

                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(vertical = 16.dp),
                        horizontalAlignment = Alignment.CenterHorizontally,
                        verticalArrangement = Arrangement.spacedBy(16.dp)
                    ) {
                        Text(
                            text = "🎉 Ders Tamamlandı!",
                            color = Color(0xFFF8FAFC),
                            fontSize = 24.sp,
                            fontWeight = FontWeight.Bold
                        )

                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.spacedBy(8.dp)
                        ) {
                            Column(
                                modifier = Modifier
                                    .weight(1f)
                                    .background(Color(0xFF0F172A), RoundedCornerShape(10.dp))
                                    .border(1.dp, Color(0xFF1E293B), RoundedCornerShape(10.dp))
                                    .padding(12.dp),
                                horizontalAlignment = Alignment.CenterHorizontally
                            ) {
                                Text("Doğruluk", color = Color(0xFF94A3B8), fontSize = 11.sp)
                                Text("%$avgAccuracy", color = Color(0xFF34D399), fontSize = 20.sp, fontWeight = FontWeight.Bold)
                            }

                            Column(
                                modifier = Modifier
                                    .weight(1f)
                                    .background(Color(0xFF0F172A), RoundedCornerShape(10.dp))
                                    .border(1.dp, Color(0xFF1E293B), RoundedCornerShape(10.dp))
                                    .padding(12.dp),
                                horizontalAlignment = Alignment.CenterHorizontally
                            ) {
                                Text("Kusursuz", color = Color(0xFF94A3B8), fontSize = 11.sp)
                                Text("$perfectCount / $totalSegments", color = Color(0xFF38BDF8), fontSize = 20.sp, fontWeight = FontWeight.Bold)
                            }

                            Column(
                                modifier = Modifier
                                    .weight(1f)
                                    .background(Color(0xFF0F172A), RoundedCornerShape(10.dp))
                                    .border(1.dp, Color(0xFF1E293B), RoundedCornerShape(10.dp))
                                    .padding(12.dp),
                                horizontalAlignment = Alignment.CenterHorizontally
                            ) {
                                Text("Tekrar", color = Color(0xFF94A3B8), fontSize = 11.sp)
                                Text("$totalReplays kez", color = Color(0xFFFBBF24), fontSize = 20.sp, fontWeight = FontWeight.Bold)
                            }
                        }

                        // Hata Defteri Özeti (F3.4)
                        if (topMistakes.isNotEmpty()) {
                            Column(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .background(Color(0xFF0F172A), RoundedCornerShape(12.dp))
                                    .border(1.dp, Color(0xFF1E293B), RoundedCornerShape(12.dp))
                                    .padding(16.dp),
                                verticalArrangement = Arrangement.spacedBy(10.dp)
                            ) {
                                Text(
                                    text = "Hata Defteri: Tekrar Edilmesi Önerilen Kelimeler",
                                    color = Color(0xFFF87171),
                                    fontSize = 13.sp,
                                    fontWeight = FontWeight.SemiBold
                                )
                                FlowRow(
                                    horizontalArrangement = Arrangement.spacedBy(8.dp),
                                    verticalArrangement = Arrangement.spacedBy(8.dp)
                                ) {
                                    topMistakes.forEach { (word, count) ->
                                        SuggestionChip(
                                            onClick = {},
                                            label = { Text("$word (${count}x)", fontSize = 12.sp, color = Color(0xFFFCA5A5)) }
                                        )
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
