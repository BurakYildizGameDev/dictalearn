package com.dictalearn.app.domain

import com.dictalearn.app.domain.words.WordModeEngine
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class WordModeTest {

    @Test
    fun tokenizeSentence_splitsAndCleansWordsCorrectly() {
        val sentence = "He packed his small, brown suitcase."
        val tokens = WordModeEngine.tokenizeSentence(sentence)

        assertEquals(6, tokens.size)

        assertEquals("He", tokens[0].raw)
        assertEquals("he", tokens[0].clean)
        assertEquals(null, tokens[0].punctuation)

        assertEquals("small,", tokens[3].raw)
        assertEquals("small", tokens[3].clean)
        assertEquals(",", tokens[3].punctuation)

        assertEquals("suitcase.", tokens[5].raw)
        assertEquals("suitcase", tokens[5].clean)
        assertEquals(".", tokens[5].punctuation)
    }

    @Test
    fun cleanWord_handlesCurlyApostrophesAndPunctuation() {
        assertEquals("it's", WordModeEngine.cleanWord("“it’s”"))
        assertEquals("don't", WordModeEngine.cleanWord("...don't!"))
        assertEquals("every", WordModeEngine.cleanWord("Every"))
    }

    @Test
    fun checkWord_validatesCorrectAndIncorrectInputs() {
        assertTrue(WordModeEngine.checkWord("every", "Every"))
        assertTrue(WordModeEngine.checkWord("don't", "don’t"))
        assertFalse(WordModeEngine.checkWord("every", "ever"))
        assertFalse(WordModeEngine.checkWord("packed", "pack"))
    }
}
