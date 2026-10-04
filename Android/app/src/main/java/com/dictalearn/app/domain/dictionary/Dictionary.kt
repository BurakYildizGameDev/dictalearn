package com.dictalearn.app.domain.dictionary

import org.json.JSONObject

data class DictionaryEntry(val headword: String, val meaning: String)

/**
 * Offline English -> Turkish dictionary (assets/lessons/dictionary.json, built by
 * tools/build_dictionary.py). Mirrors Web/src/domain/dictionary/dictionary.ts.
 */
class Dictionary(private val entries: Map<String, String>) {

    val size: Int get() = entries.size

    fun lookup(word: String): DictionaryEntry? {
        val w = normalize(word)
        if (w.isEmpty()) return null
        for (key in listOf(w) + lemmaCandidates(w)) {
            entries[key]?.let { return DictionaryEntry(key, it) }
        }
        return null
    }

    /**
     * Meaning under a solved word in word-by-word mode. Only the first [solvedCount] words are used,
     * so a phrase appears only once all of its words are solved (no hint about the next word).
     */
    fun glossForSolvedWord(words: List<String>, index: Int, solvedCount: Int): DictionaryEntry? {
        if (index >= solvedCount) return null
        return lookupInSentence(words.take(solvedCount), index)
    }

    /** Phrases of up to 4 words that include the clicked word win over the single word. */
    fun lookupInSentence(words: List<String>, index: Int): DictionaryEntry? {
        val norm = words.map(::normalize)
        for (len in minOf(4, norm.size) downTo 2) {
            val firstStart = maxOf(0, index - len + 1)
            for (start in firstStart..index) {
                if (start + len > norm.size) break
                val phrase = norm.subList(start, start + len).joinToString(" ")
                entries[phrase]?.let { return DictionaryEntry(phrase, it) }
            }
        }
        return lookup(words.getOrElse(index) { "" })
    }

    companion object {
        private val boundary = Regex("^[^\\p{L}\\p{N}']+|[^\\p{L}\\p{N}']+$")
        private val consonant = Regex("[bcdfghjklmnpqrstvwxz]")

        private val irregular = mapOf(
            "was" to "be", "were" to "be", "been" to "be", "is" to "be", "am" to "be", "are" to "be",
            "had" to "have", "has" to "have", "did" to "do", "done" to "do", "does" to "do",
            "went" to "go", "gone" to "go", "came" to "come", "saw" to "see", "seen" to "see",
            "took" to "take", "taken" to "take", "gave" to "give", "given" to "give", "made" to "make",
            "said" to "say", "told" to "tell", "knew" to "know", "known" to "know", "thought" to "think",
            "found" to "find", "felt" to "feel", "left" to "leave", "kept" to "keep", "held" to "hold",
            "stood" to "stand", "sat" to "sit", "ran" to "run", "began" to "begin", "begun" to "begin",
            "brought" to "bring", "bought" to "buy", "caught" to "catch", "taught" to "teach",
            "fought" to "fight", "heard" to "hear", "met" to "meet", "lost" to "lose", "sent" to "send",
            "spent" to "spend", "spoke" to "speak", "spoken" to "speak", "wrote" to "write",
            "written" to "write", "ate" to "eat", "eaten" to "eat", "fell" to "fall", "fallen" to "fall",
            "flew" to "fly", "flown" to "fly", "grew" to "grow", "grown" to "grow", "drew" to "draw",
            "drawn" to "draw", "threw" to "throw", "thrown" to "throw", "broke" to "break",
            "broken" to "break", "chose" to "choose", "chosen" to "choose", "rose" to "rise",
            "risen" to "rise", "woke" to "wake", "woken" to "wake", "wore" to "wear", "worn" to "wear",
            "drove" to "drive", "driven" to "drive", "rode" to "ride", "ridden" to "ride",
            "sang" to "sing", "sung" to "sing", "swam" to "swim", "drank" to "drink", "drunk" to "drink",
            "became" to "become", "slept" to "sleep", "swept" to "sweep", "wept" to "weep",
            "crept" to "creep", "built" to "build", "meant" to "mean", "led" to "lead", "fed" to "feed",
            "fled" to "flee", "hid" to "hide", "hidden" to "hide", "bit" to "bite", "shook" to "shake",
            "struck" to "strike", "stole" to "steal", "stolen" to "steal", "forgot" to "forget",
            "forgotten" to "forget", "understood" to "understand", "lay" to "lie", "lain" to "lie",
            "men" to "man", "women" to "woman", "children" to "child", "feet" to "foot",
            "teeth" to "tooth", "mice" to "mouse", "geese" to "goose", "better" to "good",
            "best" to "good", "worse" to "bad", "worst" to "bad"
        )

        fun normalize(word: String): String =
            word.lowercase()
                .replace('’', '\'').replace('‘', '\'').replace('`', '\'')
                .replace(boundary, "")
                .trim('\'')

        fun lemmaCandidates(word: String): List<String> {
            val w = normalize(word)
            val out = mutableListOf<String>()
            fun add(c: String) {
                if (c.length >= 2 && c !in out) out.add(c)
            }
            fun undouble(stem: String) {
                val n = stem.length
                if (n >= 3 && stem[n - 1] == stem[n - 2] && consonant.matches(stem[n - 1].toString())) {
                    add(stem.dropLast(1))
                }
            }
            irregular[w]?.let(::add)
            if (w.endsWith("'s")) add(w.dropLast(2))
            if (w.endsWith("s'")) add(w.dropLast(1))
            if (w.endsWith("ies") && w.length > 4) add(w.dropLast(3) + "y")
            if (w.endsWith("ied") && w.length > 4) add(w.dropLast(3) + "y")
            if (w.endsWith("es") && w.length > 3) add(w.dropLast(2))
            if (w.endsWith("s") && !w.endsWith("ss") && w.length > 3) add(w.dropLast(1))
            if (w.endsWith("ed") && w.length > 3) {
                val stem = w.dropLast(2)
                add(stem); add(stem + "e"); undouble(stem)
            }
            if (w.endsWith("ing") && w.length > 4) {
                val stem = w.dropLast(3)
                add(stem); add(stem + "e"); undouble(stem)
            }
            if (w.endsWith("ly") && w.length > 4) add(w.dropLast(2))
            if (w.endsWith("er") && w.length > 4) add(w.dropLast(2))
            if (w.endsWith("est") && w.length > 5) add(w.dropLast(3))
            return out
        }

        private const val GLOSS_MAX = 22
        private val turkish = java.util.Locale("tr")

        /** First sense of a meaning, short enough to sit under a word. */
        fun shortGloss(meaning: String): String {
            var sense = meaning.split(';').first().replace(Regex("\\([^)]*\\)"), "").trim()
            if (!sense.startsWith("-")) sense = sense.split(',').first().trim()
            if (sense.isNotEmpty()) sense = sense.substring(0, 1).lowercase(turkish) + sense.substring(1)
            if (sense.length <= GLOSS_MAX) return sense
            val cut = sense.take(GLOSS_MAX + 1)
            val space = cut.lastIndexOf(' ')
            return cut.take(if (space > 0) space else GLOSS_MAX).trim() + "…"
        }

        fun fromJson(json: String): Dictionary {
            val obj = JSONObject(json).optJSONObject("entries") ?: JSONObject()
            val map = HashMap<String, String>(obj.length() * 2)
            for (key in obj.keys()) map[key] = obj.getString(key)
            return Dictionary(map)
        }
    }
}
