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

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun StudySessionScreen(
    viewModel: StudySessionViewModel,
    modifier: Modifier = Modifier
) {
    val state by viewModel.state.collectAsState()
    val currentIndex by viewModel.currentSegmentIndex.collectAsState()
    val typedText by viewModel.typedText.collectAsState()
    val diffResult by viewModel.diffResult.collectAsState()
    val replayCount by viewModel.replayCount.collectAsState()

    var selectedSpeed by remember { mutableStateOf(1.0f) }

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
                    // Speed selectors
                    listOf(0.75f, 1.0f, 1.25f).forEach { s ->
                        FilterChip(
                            selected = selectedSpeed == s,
                            onClick = {
                                selectedSpeed = s
                                viewModel.setSpeed(s)
                            },
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

            // Audio Replay Bar
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

                if (replayCount > 0) {
                    Text(
                        text = "($replayCount kez dinlendi)",
                        color = Color(0xFF94A3B8),
                        fontSize = 12.sp
                    )
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
                            Divider(color = Color(0xFF1E293B))
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
                    val totalReplays = records.sumOf { it.replayCount }

                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(vertical = 24.dp),
                        horizontalAlignment = Alignment.CenterHorizontally,
                        verticalArrangement = Arrangement.spacedBy(16.dp)
                    ) {
                        Text(
                            text = "🎉 Ders Tamamlandı!",
                            color = Color(0xFFF8FAFC),
                            fontSize = 24.sp,
                            fontWeight = FontWeight.Bold
                        )
                        Text(
                            text = "Ortalama Doğruluk: %$avgAccuracy",
                            color = Color(0xFF34D399),
                            fontSize = 18.sp,
                            fontWeight = FontWeight.SemiBold
                        )
                        Text(
                            text = "Toplam Tekrar: $totalReplays kez",
                            color = Color(0xFF94A3B8),
                            fontSize = 14.sp
                        )
                    }
                }

                SessionState.SHADOWING -> {}
            }
        }
    }
}
