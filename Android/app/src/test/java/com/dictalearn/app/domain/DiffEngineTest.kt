package com.dictalearn.app.domain

import com.dictalearn.app.domain.diff.DiffEngine
import com.dictalearn.app.domain.diff.DiffKind
import com.dictalearn.app.domain.diff.DiffOptions
import org.junit.Assert.*
import org.junit.Test

class DiffEngineTest {

    @Test
    fun test1_perfectMatchIgnoringCase() {
        val expected = "He packed his small brown suitcase."
        val typed = "he packed his small brown suitcase"
        val result = DiffEngine.computeWordDiff(expected, typed)

        assertTrue(result.isPerfect)
        assertEquals(1.0, result.accuracy, 1e-6)
        assertEquals(6, result.expectedCount)
        assertEquals(6, result.correctCount)
        assertTrue(result.words.all { it.kind == DiffKind.EQUAL })
    }

    @Test
    fun test2_singleTypo_resultsInOneSubstitute() {
        val expected = "The morning cold hit him immediately."
        val typed = "The morning cold hit him imediately"
        val result = DiffEngine.computeWordDiff(expected, typed)

        assertFalse(result.isPerfect)
        assertEquals(5, result.correctCount)
        assertEquals(6, result.expectedCount)
        assertEquals(5.0 / 6.0, result.accuracy, 1e-4)

        val sub = result.words.find { it.kind == DiffKind.SUBSTITUTE }
        assertNotNull(sub)
        assertEquals("immediately.", sub?.expected)
        assertEquals("imediately", sub?.typed)
    }

    @Test
    fun test3_omittedWord_resultsInOneMissing() {
        val expected = "He packed his small brown suitcase."
        val typed = "He packed his brown suitcase"
        val result = DiffEngine.computeWordDiff(expected, typed)

        assertFalse(result.isPerfect)
        assertEquals(5, result.correctCount)
        assertEquals(6, result.expectedCount)

        val missing = result.words.find { it.kind == DiffKind.MISSING }
        assertNotNull(missing)
        assertEquals("small", missing?.expected)
    }

    @Test
    fun test4_extraWord_resultsInOneExtra() {
        val expected = "He opened the door."
        val typed = "He opened the the door"
        val result = DiffEngine.computeWordDiff(expected, typed)

        assertFalse(result.isPerfect)
        assertEquals(4, result.correctCount)
        assertEquals(4, result.expectedCount)

        val extra = result.words.find { it.kind == DiffKind.EXTRA }
        assertNotNull(extra)
        assertEquals("the", extra?.typed)
    }

    @Test
    fun test5_curlyQuotesNormalized() {
        val expected = "I don’t know."
        val typed = "I don't know"
        val result = DiffEngine.computeWordDiff(expected, typed)

        assertTrue(result.isPerfect)
        assertEquals(1.0, result.accuracy, 1e-6)
    }

    @Test
    fun test6_emptyTyped_resultsInAllMissing() {
        val expected = "He opened the door."
        val typed = ""
        val result = DiffEngine.computeWordDiff(expected, typed)

        assertFalse(result.isPerfect)
        assertEquals(0, result.correctCount)
        assertEquals(4, result.expectedCount)
        assertEquals(0.0, result.accuracy, 1e-6)
        assertTrue(result.words.all { it.kind == DiffKind.MISSING })
    }

    @Test
    fun test7_ignorePunctuationOption() {
        val expected = "Hello, world!"
        val typed = "hello world"

        val withPunctuation = DiffEngine.computeWordDiff(expected, typed, DiffOptions(ignorePunctuation = true))
        assertTrue(withPunctuation.isPerfect)

        val strictPunctuation = DiffEngine.computeWordDiff(expected, typed, DiffOptions(ignorePunctuation = false))
        assertFalse(strictPunctuation.isPerfect)
        assertEquals(2, strictPunctuation.words.count { it.kind == DiffKind.SUBSTITUTE })
    }

    @Test
    fun test8_ignoreCaseOption() {
        val expected = "He Opened"
        val typed = "he opened"

        val withCase = DiffEngine.computeWordDiff(expected, typed, DiffOptions(ignoreCase = true))
        assertTrue(withCase.isPerfect)

        val strictCase = DiffEngine.computeWordDiff(expected, typed, DiffOptions(ignoreCase = false))
        assertFalse(strictCase.isPerfect)
        assertEquals(2, strictCase.words.count { it.kind == DiffKind.SUBSTITUTE })
    }
}
