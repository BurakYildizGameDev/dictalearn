package com.dictalearn.app.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextDecoration
import androidx.compose.foundation.layout.ExperimentalLayoutApi
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.dictalearn.app.domain.diff.DiffKind
import com.dictalearn.app.domain.diff.DiffResult
import kotlin.math.roundToInt

@OptIn(ExperimentalLayoutApi::class)
@Composable
fun DiffViewCompose(
    diff: DiffResult,
    modifier: Modifier = Modifier
) {
    Column(
        modifier = modifier
            .fillMaxWidth()
            .background(Color(0xFF18181B), RoundedCornerShape(12.dp))
            .border(1.dp, Color(0xFF27272A), RoundedCornerShape(12.dp))
            .padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        // Header with Accuracy
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceBetween,
            verticalAlignment = Alignment.CenterVertically
        ) {
            Text(
                text = "Karşılaştırma Sonucu:",
                color = Color(0xFF94A3B8),
                fontSize = 12.sp,
                fontWeight = FontWeight.Medium
            )

            val accuracyPercent = (diff.accuracy * 100).roundToInt()
            Text(
                text = "%$accuracyPercent (${diff.correctCount}/${diff.expectedCount})",
                color = if (diff.isPerfect) Color(0xFF34D399) else Color(0xFFFBBF24),
                fontWeight = FontWeight.Bold,
                fontSize = 12.sp
            )
        }

        // Flow of Diff Words
        FlowRow(
            horizontalArrangement = Arrangement.spacedBy(8.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            diff.words.forEach { word ->
                when (word.kind) {
                    DiffKind.EQUAL -> {
                        Text(
                            text = word.expected ?: (word.typed ?: ""),
                            color = Color(0xFF34D399),
                            fontSize = 16.sp,
                            fontWeight = FontWeight.Medium
                        )
                    }
                    DiffKind.SUBSTITUTE -> {
                        Column(
                            horizontalAlignment = Alignment.CenterHorizontally,
                            modifier = Modifier
                                .background(Color(0xFF4C0519), RoundedCornerShape(4.dp))
                                .border(1.dp, Color(0xFF9F1239), RoundedCornerShape(4.dp))
                                .padding(horizontal = 6.dp, vertical = 2.dp)
                        ) {
                            Text(
                                text = word.typed ?: "",
                                color = Color(0xFFFB7185),
                                fontSize = 11.sp,
                                textDecoration = TextDecoration.LineThrough
                            )
                            Text(
                                text = word.expected ?: "",
                                color = Color(0xFF34D399),
                                fontSize = 15.sp,
                                fontWeight = FontWeight.Bold,
                                textDecoration = TextDecoration.Underline
                            )
                        }
                    }
                    DiffKind.MISSING -> {
                        Text(
                            text = "+${word.expected ?: ""}",
                            color = Color(0xFFFCD34D),
                            fontSize = 16.sp,
                            textDecoration = TextDecoration.Underline,
                            modifier = Modifier
                                .background(Color(0xFF451A03), RoundedCornerShape(4.dp))
                                .border(1.dp, Color(0xFFB45309), RoundedCornerShape(4.dp))
                                .padding(horizontal = 6.dp, vertical = 2.dp)
                        )
                    }
                    DiffKind.EXTRA -> {
                        Text(
                            text = "✕ ${word.typed ?: ""}",
                            color = Color(0xFFF43F5E),
                            fontSize = 16.sp,
                            textDecoration = TextDecoration.LineThrough,
                            modifier = Modifier
                                .background(Color(0xFF4C0519), RoundedCornerShape(4.dp))
                                .border(1.dp, Color(0xFF9F1239), RoundedCornerShape(4.dp))
                                .padding(horizontal = 6.dp, vertical = 2.dp)
                        )
                    }
                }
            }
        }
    }
}
