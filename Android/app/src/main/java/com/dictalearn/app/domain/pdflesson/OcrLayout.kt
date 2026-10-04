package com.dictalearn.app.domain.pdflesson

data class OcrWord(val text: String, val x0: Int, val x1: Int)

/** Layout and language helpers for OCR output. Mirrors Web/src/domain/pdf-lesson/ocr-layout.ts. */
object OcrLayout {
    private const val WIDE_GAP = 0.06
    private const val COLUMN_TOLERANCE = 0.025

    /**
     * Right column start. Learned from lines whose columns are clearly apart (Tesseract reads across
     * the gutter) or, when the engine already returns each column's lines separately (ML Kit), from
     * the many lines that start in the right part of the page.
     */
    private fun rightColumnStart(lines: List<List<OcrWord>>, pageWidth: Int): Int? {
        val gapStarts = mutableListOf<Int>()
        for (words in lines) {
            for (i in 1 until words.size) {
                if (words[i].x0 - words[i - 1].x1 > pageWidth * WIDE_GAP && words[i].x0 >= pageWidth * 0.35) {
                    gapStarts.add(words[i].x0)
                    break
                }
            }
        }
        if (gapStarts.size >= 2) return gapStarts.sorted()[gapStarts.size / 4]
        val lineStarts = lines.map { it.first().x0 }.filter { it >= pageWidth * 0.4 }
        val leftStarts = lines.count { it.first().x0 < pageWidth * 0.25 }
        if (lineStarts.size >= maxOf(3, (lines.size * 0.2).toInt()) && leftStarts >= 3) {
            return lineStarts.sorted()[lineStarts.size / 4]
        }
        return null
    }

    /**
     * OCR reads straight across two-column pages. Lines are split where a word starts at the right
     * column; the right column is read after the left one. Single-column pages are unchanged.
     */
    fun orderLines(lines: List<List<OcrWord>>, pageWidth: Int): String {
        val wordLines = lines.map { l -> l.filter { it.text.isNotBlank() } }.filter { it.isNotEmpty() }
        val column = rightColumnStart(wordLines, pageWidth)
        val tolerance = pageWidth * COLUMN_TOLERANCE
        val left = mutableListOf<String>()
        val right = mutableListOf<String>()
        for (words in wordLines) {
            var split = -1
            if (column != null) {
                // Left-column text never reaches the gutter: anything at/after it is the right column.
                val boundary = column - tolerance
                split = if (words[0].x0 >= boundary) 0 else words.indices.firstOrNull { i ->
                    i > 0 && words[i].x0 >= boundary && words[i].x0 > words[i - 1].x1
                } ?: -1
            }
            val leftPart = if (split == -1) words else words.subList(0, split)
            val rightPart = if (split == -1) emptyList() else words.subList(split, words.size)
            if (leftPart.isNotEmpty()) left.add(leftPart.joinToString(" ") { it.text })
            if (rightPart.isNotEmpty()) right.add(rightPart.joinToString(" ") { it.text })
        }
        return (left + right).joinToString("\n")
    }

    private val functionWords = (
        "the a an and or but of to in on at for with from by as is are was were be been it its he she " +
            "his her him they them their we our you your i me my this that these those there here not no " +
            "so if then than when what which who how all had has have do did would could should will can " +
            "into over up out about after before again very just only one"
        ).split(" ").toSet()

    private val wordRegex = Regex("[a-z']+")

    fun englishWordRatio(text: String): Double {
        val words = wordRegex.findAll(text.lowercase()).map { it.value }.toList()
        if (words.isEmpty()) return 0.0
        return words.count { it in functionWords }.toDouble() / words.size
    }

    /** Short fragments (< 4 words) cannot be judged and are allowed. */
    fun isProbablyEnglish(text: String): Boolean {
        val words = Regex("[A-Za-z']+").findAll(text).count()
        if (words < 4) return true
        return englishWordRatio(text) >= 0.12
    }
}
