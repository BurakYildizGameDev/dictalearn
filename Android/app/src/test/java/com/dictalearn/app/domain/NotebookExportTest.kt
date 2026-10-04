package com.dictalearn.app.domain

import com.dictalearn.app.domain.mistakes.NotebookExport
import org.junit.Assert.*
import org.junit.Test

class NotebookExportTest {
    private val rows = listOf(
        NotebookExport.Row("small", 3, false),
        NotebookExport.Row("quote", 1, true),
        NotebookExport.Row("zzz", 1, false)
    )
    private val meanings = mapOf("small" to "küçük", "quote" to "alıntı, \"söz\"")

    @Test
    fun csv_hasBomHeaderAndQuoting() {
        val csv = NotebookExport.csv(rows, meanings::get)
        assertTrue(csv.startsWith("\uFEFF"))
        val lines = csv.drop(1).split("\r\n")
        assertEquals("word,meaning,count,type", lines[0])
        assertEquals("small,küçük,3,hata", lines[1])
        assertEquals("quote,\"alıntı, \"\"söz\"\"\",1,bilmiyorum", lines[2])
        assertEquals("zzz,,1,hata", lines[3])
    }

    @Test
    fun anki_skipsWordsWithoutMeaning() {
        val tsv = NotebookExport.ankiTsv(rows, meanings::get)
        assertEquals("#separator:tab\n#html:false\nsmall\tküçük\nquote\talıntı, \"söz\"\n", tsv)
    }
}
