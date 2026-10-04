package com.dictalearn.app.domain.mistakes

/** Notebook export: CSV and Anki's tab-separated import format. Mirrors Web/src/domain/mistakes/export.ts. */
object NotebookExport {
    data class Row(val word: String, val count: Int, val unknown: Boolean)

    private fun csvField(v: String) = if (Regex("[\",\r\n]").containsMatchIn(v)) "\"" + v.replace("\"", "\"\"") + "\"" else v

    fun csv(rows: List<Row>, meaningOf: (String) -> String?): String {
        val lines = mutableListOf(listOf("word", "meaning", "count", "type"))
        rows.forEach { lines.add(listOf(it.word, meaningOf(it.word) ?: "", it.count.toString(), if (it.unknown) "bilmiyorum" else "hata")) }
        return "\uFEFF" + lines.joinToString("\r\n") { l -> l.joinToString(",") { csvField(it) } }
    }

    fun ankiTsv(rows: List<Row>, meaningOf: (String) -> String?): String {
        fun clean(s: String) = s.replace(Regex("[\t\r\n]+"), " ").trim()
        val cards = rows.mapNotNull { r -> meaningOf(r.word)?.let { "${clean(r.word)}\t${clean(it)}" } }
        return (listOf("#separator:tab", "#html:false") + cards).joinToString("\n") + "\n"
    }
}
