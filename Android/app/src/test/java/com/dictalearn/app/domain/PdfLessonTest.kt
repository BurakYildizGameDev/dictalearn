package com.dictalearn.app.domain

import com.dictalearn.app.domain.pdflesson.OcrLayout
import com.dictalearn.app.domain.pdflesson.OcrWord
import com.dictalearn.app.domain.pdflesson.PdfLesson
import org.junit.Assert.*
import org.junit.Test

class PdfLessonTest {

    @Test
    fun extractSentences_splitsProse_andJoinsHyphenation() {
        val text = "Tom packed his bag. Then he left the house!\nHe walked to the sta-\ntion quickly. \"Wait for me,\" said Ann."
        assertEquals(
            listOf("Tom packed his bag.", "Then he left the house!", "He walked to the station quickly.", "\"Wait for me,\" said Ann."),
            PdfLesson.extractSentences(text)
        )
    }

    @Test
    fun extractSentences_keepsAbbreviations() {
        assertEquals(
            listOf("Mr. Holmes met Dr. Watson at the door.", "They talked for hours."),
            PdfLesson.extractSentences("Mr. Holmes met Dr. Watson at the door. They talked for hours.")
        )
    }

    @Test
    fun extractSentences_usesNumberedBlocks_andDropsTurkishEvenWithoutTurkishLetters() {
        val text = listOf(
            "[1] \"She said that she would dance with me,\" cried the",
            "young Student.",
            "[2] \"Yet in all my garden there is no red rose.\"",
            "[3] He was sad and his life was ruined.",
            "[4] The Nightingale heard his sorrowful words.",
            "[5] She flew over the garden like a shadow.",
            "[1] Geng Ogrenci \"Benimle dans edecegini soyledi,\" diye yakindi.",
            "[2] \"Fakat bahgemde hic kirmizi gul yok.\"",
            "[3] Hayati sefil ve harap oldu.",
            "[4] Bulbul onun kederli sozlerini isitti.",
            "[5] Bahcenin uzerinden bir golge gibi uctu."
        ).joinToString("\n")
        assertEquals(
            listOf(
                "\"She said that she would dance with me,\" cried the young Student.",
                "\"Yet in all my garden there is no red rose.\"",
                "He was sad and his life was ruined.",
                "The Nightingale heard his sorrowful words.",
                "She flew over the garden like a shadow."
            ),
            PdfLesson.extractSentences(text)
        )
    }

    @Test
    fun extractSentences_understandsOcrMangledNumbers() {
        val text = listOf(
            "[1] The student cried in the garden.",
            "(2] The bird heard all of his words.",
            "[s] She flew over the dark trees.",
            "[8j He looked at the red rose.",
            "[10) It was the most beautiful rose.",
            "[u] The night was cold and very long."
        ).joinToString("\n")
        assertEquals(
            listOf(
                "The student cried in the garden.", "The bird heard all of his words.", "She flew over the dark trees.",
                "He looked at the red rose.", "It was the most beautiful rose.", "The night was cold and very long."
            ),
            PdfLesson.extractSentences(text)
        )
    }

    @Test
    fun extractSentences_separatesHeadings_andFallsBackToLines() {
        val prose = "Contents\nAbout this book\nYou will find each of these words in bold.\nMeet the Flyers\nThe children love going to the park."
        assertEquals(
            listOf("You will find each of these words in bold.", "The children love going to the park."),
            PdfLesson.extractSentences(prose)
        )
        val wordList = "Animals\nthe big brown bear\na small grey mouse\na tall giraffe\nan old horse\na fast rabbit\n7"
        assertEquals(
            listOf("the big brown bear", "a small grey mouse", "a tall giraffe", "an old horse", "a fast rabbit"),
            PdfLesson.extractSentences(wordList)
        )
        assertTrue(PdfLesson.extractSentences("  \n ").isEmpty())
    }

    @Test
    fun buildLesson_hasSyntheticIntegerTimings() {
        val lesson = PdfLesson.buildLesson("pdf_x", "Benim Kitabım.pdf", listOf("One two three.", "Four five six."))
        assertEquals("Benim Kitabım", lesson.title)
        assertEquals(listOf(0, PdfLesson.SEGMENT_MS), lesson.segments.map { it.startMs })
        assertEquals(PdfLesson.SEGMENT_MS - 1, lesson.segments[0].endMs)
    }

    @Test
    fun mergeSentences_onlyAppends() {
        assertEquals(
            listOf("A b c.", "D e f.", "G h i."),
            PdfLesson.mergeSentences(listOf("A b c.", "D e f."), listOf("a b c.", "G h i.", "D e f."))
        )
        assertEquals(25, PdfLesson.firstBatchSize(120))
        assertEquals(7, PdfLesson.firstBatchSize(7))
    }

    @Test
    fun ocrLayout_splitsAtLearnedColumnStart() {
        fun w(t: String, x0: Int, x1: Int) = OcrWord(t, x0, x1)
        val lines = listOf(
            listOf(w("short", 10, 60), w("line.", 65, 110), w("Kısa", 520, 560)),
            listOf(w("another", 10, 80), w("one.", 85, 120), w("Diğer", 520, 570)),
            listOf(w("[1]", 10, 40), w("A", 45, 55), w("very", 60, 100), w("long", 105, 470), w("cried", 475, 508), w("[1]", 520, 545), w("Genç", 550, 600))
        )
        assertEquals(
            "short line.\nanother one.\n[1] A very long cried\nKısa\nDiğer\n[1] Genç",
            OcrLayout.orderLines(lines, 1000)
        )
        assertEquals("Chapter One", OcrLayout.orderLines(listOf(listOf(w("Chapter", 10, 120), w("One", 600, 680))), 1000))
    }

    @Test
    fun ocrLayout_usesLineStarts_whenColumnsComeAsSeparateLines() {
        fun w(t: String, x0: Int, x1: Int) = OcrWord(t, x0, x1)
        // ML Kit style: each column's line is its own line, sorted top to bottom (interleaved)
        val lines = listOf(
            listOf(w("[1]", 20, 50), w("She", 55, 90), w("said", 95, 140)),
            listOf(w("[1]", 520, 550), w("Genç", 555, 600)),
            listOf(w("young", 20, 80), w("Student.", 85, 160)),
            listOf(w("diye", 520, 560), w("yakındı.", 565, 640)),
            listOf(w("[2]", 20, 50), w("Yet", 55, 90)),
            listOf(w("[2]", 520, 550), w("Fakat", 555, 610))
        )
        assertEquals(
            "[1] She said\nyoung Student.\n[2] Yet\n[1] Genç\ndiye yakındı.\n[2] Fakat",
            OcrLayout.orderLines(lines, 1000)
        )
    }

    @Test
    fun englishDetection_byFunctionWords() {
        assertTrue(OcrLayout.isProbablyEnglish("From her high nest in the tree, the gentle Nightingale heard his words."))
        assertFalse(OcrLayout.isProbablyEnglish("Fakat bitin bahgemde higbir yerde tek bir kirmizi gll dahi bulunmuyor."))
        assertTrue(OcrLayout.isProbablyEnglish("a tall giraffe"))
    }
}
