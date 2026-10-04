package com.dictalearn.app.domain

import com.dictalearn.app.domain.library.LessonCatalog
import org.junit.Assert.*
import org.junit.Test

class LessonCatalogTest {

    @Test
    fun catalog_hasUniqueIds_and36GradedBooks() {
        val ids = LessonCatalog.books.map { it.id }
        assertEquals(ids.size, ids.toSet().size)
        val graded = LessonCatalog.books.filter { it.level > 0 }
        assertEquals(36, graded.size)
        graded.forEach { assertEquals(it.pages * 20, it.sentences) }
    }

    @Test
    fun audioPath_pointsToMp3NotWav() {
        val book = LessonCatalog.find("book_32_dracula")!!
        assertEquals("lessons/book_32_dracula/audio.mp3", book.audioAssetPath)
        assertEquals("lessons/book_32_dracula/lesson.json", book.lessonAssetPath)
        assertEquals("lessons/book_32_dracula/book_32_dracula.pdf", book.pdfAssetPath)
        assertNull(LessonCatalog.find("sample_ch01")!!.pdfAssetPath)
    }

    @Test
    fun filter_byLevelAndQuery_isCaseAndAccentInsensitive() {
        val level2 = LessonCatalog.filter(LessonCatalog.books, level = 2, query = "")
        assertTrue(level2.isNotEmpty())
        assertTrue(level2.all { it.level == 2 })

        val dracula = LessonCatalog.filter(LessonCatalog.books, level = null, query = "DRACULA")
        assertEquals(listOf("book_32_dracula"), dracula.map { it.id })

        val ghost = LessonCatalog.filter(LessonCatalog.books, level = null, query = "hayalet")
        assertTrue(ghost.any { it.id == "book_35_the_canterville_ghost" })

        val cagri = LessonCatalog.filter(LessonCatalog.books, level = null, query = "cagrisi")
        assertTrue(cagri.any { it.id == "book_30_the_call_of_the_wild" })
    }

    @Test
    fun onlyAvailable_dropsBooksMissingFromAssets() {
        val available = LessonCatalog.onlyAvailable(setOf("book_01_the_happy_prince", "sample_ch01"))
        assertEquals(listOf("book_01_the_happy_prince", "sample_ch01"), available.map { it.id })
    }
}
