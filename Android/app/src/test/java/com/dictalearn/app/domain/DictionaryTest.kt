package com.dictalearn.app.domain

import com.dictalearn.app.domain.dictionary.Dictionary
import com.dictalearn.app.domain.dictionary.DictionaryEntry
import org.junit.Assert.*
import org.junit.Test

class DictionaryTest {

    private val dict = Dictionary(
        mapOf(
            "pack" to "toplamak",
            "story" to "hikâye",
            "stand" to "ayakta durmak",
            "stop" to "durmak",
            "make" to "yapmak",
            "happy" to "mutlu",
            "drift apart" to "birbirinden uzaklaşmak",
            "high above" to "çok yukarısında",
            "box" to "kutu",
            "run" to "koşmak"
        )
    )

    @Test
    fun normalize_stripsPunctuationAndUnifiesApostrophes() {
        assertEquals("happy", Dictionary.normalize("“Happy,”"))
        assertEquals("o'clock", Dictionary.normalize("O’clock."))
        assertEquals("", Dictionary.normalize("..."))
    }

    @Test
    fun lemmaCandidates_coverRegularAndIrregularForms() {
        assertTrue("pack" in Dictionary.lemmaCandidates("packed"))
        assertTrue("story" in Dictionary.lemmaCandidates("stories"))
        assertTrue("stop" in Dictionary.lemmaCandidates("stopped"))
        assertTrue("make" in Dictionary.lemmaCandidates("making"))
        assertTrue("box" in Dictionary.lemmaCandidates("boxes"))
        assertTrue("run" in Dictionary.lemmaCandidates("running"))
        assertTrue("prince" in Dictionary.lemmaCandidates("prince's"))
        assertTrue("stand" in Dictionary.lemmaCandidates("stood"))
    }

    @Test
    fun lookup_findsExactAndInflectedWords() {
        assertEquals(DictionaryEntry("happy", "mutlu"), dict.lookup("Happy!"))
        assertEquals(DictionaryEntry("pack", "toplamak"), dict.lookup("packed"))
        assertEquals(DictionaryEntry("stand", "ayakta durmak"), dict.lookup("stood"))
        assertNull(dict.lookup("zyzzyva"))
        assertNull(dict.lookup(""))
    }

    @Test
    fun lookupInSentence_prefersLongestPhraseContainingWord() {
        assertEquals("drift apart", dict.lookupInSentence(listOf("They", "began", "to", "drift", "apart."), 4)?.headword)
        assertEquals("high above", dict.lookupInSentence(listOf("High", "above", "the", "city"), 0)?.headword)
        assertEquals("pack", dict.lookupInSentence(listOf("He", "packed", "it"), 1)?.headword)
    }

    @Test
    fun glossForSolvedWord_neverHintsTheNextWord() {
        val words = listOf("They", "began", "to", "drift", "apart.")
        assertNull(dict.glossForSolvedWord(words, 3, 4))
        assertEquals("drift apart", dict.glossForSolvedWord(words, 3, 5)?.headword)
        assertEquals("pack", dict.glossForSolvedWord(listOf("He", "packed", "it"), 1, 2)?.headword)
    }

    @Test
    fun shortGloss_keepsFirstSense() {
        assertEquals("toplamak", Dictionary.shortGloss("toplamak, paketlemek"))
        assertEquals("-de, -da", Dictionary.shortGloss("-de, -da; içinde"))
        assertEquals("belirli tanımlık", Dictionary.shortGloss("belirli tanımlık (o, şu)"))
        assertEquals("kırlangıç kuşu", Dictionary.shortGloss("Kırlangıç kuşu"))
        assertEquals("çok uzun bir açıklama…", Dictionary.shortGloss("çok uzun bir açıklama metni burada devam ediyor"))
    }

    @Test
    fun fromJson_readsSharedDictionaryFile() {
        val parsed = Dictionary.fromJson("""{"version":1,"entries":{"cold":"soğuk","hit":"vurmak"}}""")
        assertEquals(2, parsed.size)
        assertEquals("soğuk", parsed.lookup("Cold.")?.meaning)
    }
}
