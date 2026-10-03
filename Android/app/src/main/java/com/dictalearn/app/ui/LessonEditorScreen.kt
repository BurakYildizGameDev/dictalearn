package com.dictalearn.app.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material.icons.filled.PlayArrow
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.dictalearn.app.domain.model.Lesson
import com.dictalearn.app.domain.model.Segment
import com.dictalearn.app.domain.parser.LessonParser

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun LessonEditorScreen(
    initialLesson: Lesson? = null,
    onStartLesson: (Lesson) -> Unit,
    onCancel: () -> Unit,
    modifier: Modifier = Modifier
) {
    var title by remember { mutableStateOf(initialLesson?.title ?: "Yeni Ders") }
    var lessonId by remember { mutableStateOf(initialLesson?.lessonId ?: "custom_lesson_01") }
    var sourceLang by remember { mutableStateOf(initialLesson?.sourceLang ?: "en") }
    var targetLang by remember { mutableStateOf(initialLesson?.targetLang ?: "tr") }
    var audioFile by remember { mutableStateOf(initialLesson?.audioFile ?: "audio.wav") }

    var segments by remember {
        mutableStateOf(
            initialLesson?.segments ?: listOf(
                Segment(
                    id = 1,
                    startMs = 0,
                    endMs = 3000,
                    text = "He packed his suitcase.",
                    translation = "Bavulunu topladı."
                )
            )
        )
    }

    var validationErrors by remember { mutableStateOf<List<String>>(emptyList()) }

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Text(
                        text = "Ders Düzenleyici",
                        fontSize = 16.sp,
                        fontWeight = FontWeight.Bold,
                        color = Color(0xFFF8FAFC)
                    )
                },
                navigationIcon = {
                    IconButton(onClick = onCancel) {
                        Icon(
                            imageVector = Icons.AutoMirrored.Filled.ArrowBack,
                            contentDescription = "Geri Dön",
                            tint = Color(0xFFF8FAFC)
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
            // Validation errors
            if (validationErrors.isNotEmpty()) {
                Column(
                    modifier = Modifier
                        .fillMaxWidth()
                        .background(Color(0xFF450A0A), RoundedCornerShape(8.dp))
                        .border(1.dp, Color(0xFF991B1B), RoundedCornerShape(8.dp))
                        .padding(12.dp)
                ) {
                    Text(
                        text = "Lütfen hataları düzeltin:",
                        color = Color(0xFFFCA5A5),
                        fontWeight = FontWeight.Bold,
                        fontSize = 12.sp
                    )
                    validationErrors.forEach { err ->
                        Text(text = "• $err", color = Color(0xFFFECACA), fontSize = 11.sp)
                    }
                }
            }

            // Metadata card
            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .background(Color(0xFF0F172A), RoundedCornerShape(12.dp))
                    .border(1.dp, Color(0xFF1E293B), RoundedCornerShape(12.dp))
                    .padding(16.dp),
                verticalArrangement = Arrangement.spacedBy(10.dp)
            ) {
                Text(
                    text = "DERS BİLGİLERİ",
                    color = Color(0xFF94A3B8),
                    fontSize = 11.sp,
                    fontWeight = FontWeight.Bold
                )

                OutlinedTextField(
                    value = title,
                    onValueChange = { title = it },
                    label = { Text("Ders Başlığı") },
                    modifier = Modifier.fillMaxWidth()
                )

                OutlinedTextField(
                    value = lessonId,
                    onValueChange = { lessonId = it },
                    label = { Text("Ders ID") },
                    modifier = Modifier.fillMaxWidth()
                )
            }

            // Segments header
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text(
                    text = "Cümleler (${segments.size})",
                    color = Color(0xFFF8FAFC),
                    fontSize = 15.sp,
                    fontWeight = FontWeight.Bold
                )

                Button(
                    onClick = {
                        val last = segments.lastOrNull()
                        val nextStart = if (last != null) last.endMs + 200 else 0
                        val nextEnd = nextStart + 3000
                        val newSeg = Segment(
                            id = segments.size + 1,
                            startMs = nextStart,
                            endMs = nextEnd,
                            text = "",
                            translation = ""
                        )
                        segments = segments + newSeg
                    },
                    colors = ButtonDefaults.buttonColors(containerColor = Color(0xFF059669)),
                    shape = RoundedCornerShape(8.dp)
                ) {
                    Icon(Icons.Default.Add, contentDescription = null, modifier = Modifier.size(16.dp))
                    Spacer(modifier = Modifier.width(4.dp))
                    Text("Cümle Ekle", fontSize = 12.sp)
                }
            }

            // Segments list
            segments.forEachIndexed { index, seg ->
                Column(
                    modifier = Modifier
                        .fillMaxWidth()
                        .background(Color(0xFF0F172A), RoundedCornerShape(10.dp))
                        .border(1.dp, Color(0xFF1E293B), RoundedCornerShape(10.dp))
                        .padding(12.dp),
                    verticalArrangement = Arrangement.spacedBy(8.dp)
                ) {
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Text(
                            text = "Cümle #${index + 1}",
                            color = Color(0xFF6366F1),
                            fontSize = 12.sp,
                            fontWeight = FontWeight.Bold
                        )

                        if (segments.size > 1) {
                            IconButton(
                                onClick = {
                                    val filtered = segments.filterIndexed { i, _ -> i != index }
                                    segments = filtered.mapIndexed { i, s -> s.copy(id = i + 1) }
                                },
                                modifier = Modifier.size(24.dp)
                            ) {
                                Icon(
                                    Icons.Default.Delete,
                                    contentDescription = "Sil",
                                    tint = Color(0xFFEF4444),
                                    modifier = Modifier.size(16.dp)
                                )
                            }
                        }
                    }

                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.spacedBy(8.dp)
                    ) {
                        OutlinedTextField(
                            value = seg.startMs.toString(),
                            onValueChange = { str ->
                                val ms = str.toIntOrNull() ?: 0
                                val updated = segments.toMutableList()
                                updated[index] = seg.copy(startMs = ms)
                                segments = updated
                            },
                            label = { Text("Başlangıç (ms)", fontSize = 10.sp) },
                            keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                            modifier = Modifier.weight(1f)
                        )

                        OutlinedTextField(
                            value = seg.endMs.toString(),
                            onValueChange = { str ->
                                val ms = str.toIntOrNull() ?: 0
                                val updated = segments.toMutableList()
                                updated[index] = seg.copy(endMs = ms)
                                segments = updated
                            },
                            label = { Text("Bitiş (ms)", fontSize = 10.sp) },
                            keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                            modifier = Modifier.weight(1f)
                        )
                    }

                    OutlinedTextField(
                        value = seg.text,
                        onValueChange = { str ->
                            val updated = segments.toMutableList()
                            updated[index] = seg.copy(text = str)
                            segments = updated
                        },
                        label = { Text("İngilizce Cümle", fontSize = 11.sp) },
                        modifier = Modifier.fillMaxWidth()
                    )

                    OutlinedTextField(
                        value = seg.translation ?: "",
                        onValueChange = { str ->
                            val updated = segments.toMutableList()
                            updated[index] = seg.copy(translation = str.ifBlank { null })
                            segments = updated
                        },
                        label = { Text("Türkçe Çeviri (İsteğe bağlı)", fontSize = 11.sp) },
                        modifier = Modifier.fillMaxWidth()
                    )
                }
            }

            Spacer(modifier = Modifier.height(8.dp))

            // Start lesson button
            Button(
                onClick = {
                    val lesson = Lesson(
                        schemaVersion = 1,
                        lessonId = lessonId.trim().ifEmpty { "custom_lesson" },
                        title = title.trim().ifEmpty { "İsimsiz Ders" },
                        sourceLang = sourceLang,
                        targetLang = targetLang,
                        audioFile = audioFile,
                        segments = segments.mapIndexed { i, s ->
                            s.copy(id = i + 1, text = s.text.trim())
                        }
                    )

                    val jsonStr = LessonParser.toJson(lesson)
                    val validation = LessonParser.parse(jsonStr)

                    if (!validation.isValid || validation.lesson == null) {
                        validationErrors = validation.errors
                    } else {
                        validationErrors = emptyList()
                        onStartLesson(validation.lesson)
                    }
                },
                modifier = Modifier
                    .fillMaxWidth()
                    .height(48.dp),
                colors = ButtonDefaults.buttonColors(containerColor = Color(0xFF4F46E5)),
                shape = RoundedCornerShape(10.dp)
            ) {
                Icon(Icons.Default.PlayArrow, contentDescription = null, modifier = Modifier.size(18.dp))
                Spacer(modifier = Modifier.width(6.dp))
                Text("Dersi Başlat", fontSize = 14.sp, fontWeight = FontWeight.SemiBold)
            }
        }
    }
}
