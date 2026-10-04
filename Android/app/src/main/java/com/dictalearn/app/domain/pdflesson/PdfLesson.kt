package com.dictalearn.app.domain.pdflesson

import com.dictalearn.app.domain.model.Attribution
import com.dictalearn.app.domain.model.Lesson
import com.dictalearn.app.domain.model.Segment

/**
 * Turns the text of a user's PDF into a dictation lesson. Mirrors
 * Web/src/domain/pdf-lesson/pdf-lesson.ts and progressive.ts.
 */
object PdfLesson {
    /** Synthetic slot per segment; the speech engine maps start_ms back to the sentence. */
    const val SEGMENT_MS = 10_000

    /** Pages processed before the lesson opens; the rest continue in the background. */
    const val FIRST_BATCH_PAGES = 25

    private const val MIN_WORDS = 3
    private const val MAX_WORDS = 40
    private const val DOT = ''

    private val abbreviations = listOf("Mr", "Mrs", "Ms", "Dr", "St", "Mt", "Jr", "Sr", "Prof", "Capt", "Col", "Gen", "vs", "etc", "No")
    private val turkishChars = Regex("[çğışöüÇĞİŞÖÜ]")
    private val endsSentence = Regex("[.!?:;][\"”’)]?$")
    private val endsTerminal = Regex("[.!?][\"”’)]?$")
    private val startsUpper = Regex("^[\"“‘(]?[A-Z]")
    private val sentenceBreak = Regex("(?<=[.!?][\"”’)]?)\\s+(?=[\"“‘(]?[A-Z0-9])")
    private val numberMarker = Regex("\\[\\d{1,4}]")

    fun firstBatchSize(totalPages: Int): Int = totalPages.coerceIn(0, FIRST_BATCH_PAGES)

    private fun wordCount(s: String) = s.split(Regex("\\s+")).count { it.isNotBlank() }

    private fun looksLikeEnglish(s: String): Boolean {
        if (turkishChars.containsMatchIn(s)) return false
        if (!s.any { it in 'a'..'z' }) return false
        val compact = s.filterNot { it.isWhitespace() }
        if (compact.isEmpty() || compact.count { it in 'a'..'z' || it in 'A'..'Z' }.toDouble() / compact.length <= 0.6) return false
        return OcrLayout.isProbablyEnglish(s)
    }

    private fun validSentence(s: String) = wordCount(s) in MIN_WORDS..MAX_WORDS && looksLikeEnglish(s)

    private fun normalize(text: String) = text
        .replace("\r", "")
        .replace(Regex("(\\w)-\\n(\\w)"), "$1$2")
        // OCR reads "[5]" as "[s]", "(2]", "[8j", "[10)"…: normalize line-leading markers
        .replace(Regex("(?m)^[\\[(][0-9A-Za-z]{1,3}[\\])jJ]\\s*"), "[0] ")
        .replace(Regex("[ \\t]+"), " ")

    private fun splitSentences(paragraph: String): List<String> {
        var protectedText = paragraph
        for (abbr in abbreviations) {
            protectedText = protectedText.replace(Regex("\\b$abbr\\."), "$abbr$DOT")
        }
        return protectedText.split(sentenceBreak).map { it.replace(DOT, '.').trim() }.filter { it.isNotEmpty() }
    }

    /** Parallel-text PDFs number sentences ("[12] English…" then "[12] Türkçe…"); judge whole blocks. */
    private fun numberedBlocks(normalized: String): List<String>? {
        val parts = normalized.split(numberMarker)
        if (parts.size < 6) return null
        return parts.drop(1)
            .map { it.replace(Regex("\\s+"), " ").trim() }
            .filter { it.isNotEmpty() && !turkishChars.containsMatchIn(it) }
            .flatMap { splitSentences(it) }
            .filter(::validSentence)
    }

    /** Short capitalised lines without end punctuation followed by another capitalised line are headings. */
    private fun toParagraphs(lines: List<String>): List<String> {
        val paragraphs = mutableListOf<String>()
        var current = mutableListOf<String>()
        lines.forEachIndexed { i, line ->
            val next = lines.getOrElse(i + 1) { "" }
            val heading = wordCount(line) <= 8 && !endsSentence.containsMatchIn(line) &&
                startsUpper.containsMatchIn(line) && startsUpper.containsMatchIn(next)
            if (heading) {
                if (current.isNotEmpty()) paragraphs.add(current.joinToString(" "))
                current = mutableListOf()
            } else {
                current.add(line)
            }
        }
        if (current.isNotEmpty()) paragraphs.add(current.joinToString(" "))
        return paragraphs
    }

    private fun dedupe(items: List<String>): List<String> {
        val seen = HashSet<String>()
        return items.filter { seen.add(it.lowercase()) }
    }

    fun extractSentences(text: String): List<String> {
        val normalized = normalize(text)
        numberedBlocks(normalized)?.let { if (it.size >= 5) return dedupe(it) }

        val englishLines = normalized.split("\n").map { it.trim() }.filter { it.isNotEmpty() && looksLikeEnglish(it) }
        val sentences = toParagraphs(englishLines)
            .flatMap { splitSentences(it) }
            .filter { endsTerminal.containsMatchIn(it) }
            .filter(::validSentence)
        if (sentences.size >= 5 || (sentences.isNotEmpty() && englishLines.size < 10)) return dedupe(sentences)

        val lines = englishLines.filter { wordCount(it) in 2..20 }
        return dedupe(if (lines.isNotEmpty()) lines else sentences)
    }

    fun mergeSentences(existing: List<String>, incoming: List<String>): List<String> {
        val seen = existing.map { it.lowercase() }.toHashSet()
        val merged = existing.toMutableList()
        for (s in incoming) if (seen.add(s.lowercase())) merged.add(s)
        return merged
    }

    fun buildLesson(lessonId: String, fileName: String, sentences: List<String>) = Lesson(
        schemaVersion = 1,
        lessonId = lessonId,
        title = fileName.replace(Regex("\\.pdf$", RegexOption.IGNORE_CASE), ""),
        sourceLang = "en",
        targetLang = "tr",
        audioFile = "speech-synthesis",
        attribution = Attribution(source = "Kullanıcının PDF dosyası: $fileName", license = "Personal"),
        segments = sentences.mapIndexed { i, text ->
            Segment(id = i + 1, startMs = i * SEGMENT_MS, endMs = (i + 1) * SEGMENT_MS - 1, text = text)
        }
    )
}
