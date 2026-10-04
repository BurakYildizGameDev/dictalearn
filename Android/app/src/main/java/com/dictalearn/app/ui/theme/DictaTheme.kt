package com.dictalearn.app.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Typography
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.sp

/** Palette shared with the web app (zinc neutrals, indigo accent). */
object Dicta {
    val Background = Color(0xFF09090B)
    val Surface = Color(0xFF18181B)
    val SurfaceHigh = Color(0xFF27272A)
    val Outline = Color(0x1AFFFFFF)
    val TextPrimary = Color(0xFFF4F4F5)
    val TextSecondary = Color(0xFFA1A1AA)
    val TextMuted = Color(0xFF71717A)
    val Accent = Color(0xFF818CF8)
    val AccentStrong = Color(0xFF6366F1)
    val Success = Color(0xFF6EE7B7)
    val Warning = Color(0xFFFCD34D)
    val Error = Color(0xFFFDA4AF)

    private val covers = listOf(
        Color(0xFFF43F5E) to Color(0xFFFB923C),
        Color(0xFF6366F1) to Color(0xFF38BDF8),
        Color(0xFF10B981) to Color(0xFF5EEAD4),
        Color(0xFFF59E0B) to Color(0xFFFDE047),
        Color(0xFFD946EF) to Color(0xFFF472B6),
        Color(0xFF06B6D4) to Color(0xFF60A5FA),
        Color(0xFF8B5CF6) to Color(0xFFC084FC),
        Color(0xFF84CC16) to Color(0xFF4ADE80)
    )

    /** Same id → same cover gradient (same hash as the web app). */
    fun coverBrush(id: String): Brush {
        var hash = 0
        for (ch in id) hash = hash * 31 + ch.code
        val (a, b) = covers[Math.floorMod(hash, covers.size)]
        return Brush.linearGradient(listOf(a.copy(alpha = 0.85f), b.copy(alpha = 0.75f)))
    }
}

private val colors = darkColorScheme(
    primary = Dicta.AccentStrong,
    onPrimary = Color.White,
    secondary = Dicta.Success,
    background = Dicta.Background,
    onBackground = Dicta.TextPrimary,
    surface = Dicta.Background,
    onSurface = Dicta.TextPrimary,
    surfaceVariant = Dicta.Surface,
    onSurfaceVariant = Dicta.TextSecondary,
    surfaceContainer = Dicta.Surface,
    surfaceContainerHigh = Dicta.SurfaceHigh,
    secondaryContainer = Dicta.SurfaceHigh,
    onSecondaryContainer = Dicta.TextPrimary,
    outline = Color(0xFF3F3F46),
    outlineVariant = Color(0xFF27272A),
    error = Dicta.Error
)

val SerifStyle = TextStyle(fontFamily = FontFamily.Serif)

private val typography = Typography(
    headlineLarge = TextStyle(fontFamily = FontFamily.Serif, fontSize = 32.sp, lineHeight = 38.sp),
    headlineSmall = TextStyle(fontFamily = FontFamily.Serif, fontSize = 22.sp, lineHeight = 28.sp),
    titleLarge = TextStyle(fontFamily = FontFamily.Serif, fontSize = 20.sp, lineHeight = 26.sp),
    titleMedium = TextStyle(fontWeight = FontWeight.Medium, fontSize = 15.sp),
    labelSmall = TextStyle(fontWeight = FontWeight.SemiBold, fontSize = 11.sp, letterSpacing = 1.2.sp)
)

@Composable
fun DictaTheme(content: @Composable () -> Unit) {
    MaterialTheme(colorScheme = colors, typography = typography, content = content)
}
