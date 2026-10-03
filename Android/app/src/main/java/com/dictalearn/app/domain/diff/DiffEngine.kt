package com.dictalearn.app.domain.diff

import kotlin.math.abs
import kotlin.math.min

object DiffEngine {

    fun normalizeWord(word: String, options: DiffOptions): String {
        var w = word.replace('’', '\'').replace('‘', '\'').replace('“', '"').replace('”', '"')

        if (options.ignorePunctuation) {
            // Strip leading and trailing punctuation, keeping internal apostrophes and hyphens
            w = w.trim { !it.isLetterOrDigit() }
        }

        if (options.ignoreCase) {
            w = w.lowercase()
        }

        return w
    }

    private fun splitWords(text: String): List<String> {
        val clean = text.trim().replace('’', '\'').replace('‘', '\'').replace('“', '"').replace('”', '"')
        if (clean.isEmpty()) return emptyList()
        return clean.split("\\s+".toRegex()).filter { it.isNotEmpty() }
    }

    fun computeWordDiff(
        expectedText: String,
        typedText: String,
        options: DiffOptions = DiffOptions()
    ): DiffResult {
        val expectedWords = splitWords(expectedText)
        val typedWords = splitWords(typedText)

        val n = expectedWords.size
        val m = typedWords.size

        if (n == 0 && m == 0) {
            return DiffResult(
                words = emptyList(),
                correctCount = 0,
                expectedCount = 0,
                accuracy = 1.0,
                isPerfect = true
            )
        }

        if (n == 0) {
            val words = typedWords.map { DiffWord(kind = DiffKind.EXTRA, typed = it) }
            return DiffResult(
                words = words,
                correctCount = 0,
                expectedCount = 0,
                accuracy = 0.0,
                isPerfect = false
            )
        }

        if (m == 0) {
            val words = expectedWords.map { DiffWord(kind = DiffKind.MISSING, expected = it) }
            return DiffResult(
                words = words,
                correctCount = 0,
                expectedCount = n,
                accuracy = 0.0,
                isPerfect = false
            )
        }

        val normExpected = expectedWords.map { normalizeWord(it, options) }
        val normTyped = typedWords.map { normalizeWord(it, options) }

        val dp = Array(n + 1) { DoubleArray(m + 1) }

        for (i in 0..n) dp[i][0] = i.toDouble()
        for (j in 0..m) dp[0][j] = j.toDouble()

        for (i in 1..n) {
            for (j in 1..m) {
                if (normExpected[i - 1] == normTyped[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1]
                } else {
                    val subCost = dp[i - 1][j - 1] + 1.2
                    val delCost = dp[i - 1][j] + 1.0
                    val insCost = dp[i][j - 1] + 1.0
                    dp[i][j] = min(subCost, min(delCost, insCost))
                }
            }
        }

        val resultWords = mutableListOf<DiffWord>()
        var i = n
        var j = m

        while (i > 0 || j > 0) {
            if (i > 0 && j > 0) {
                if (normExpected[i - 1] == normTyped[j - 1]) {
                    resultWords.add(
                        DiffWord(
                            kind = DiffKind.EQUAL,
                            expected = expectedWords[i - 1],
                            typed = typedWords[j - 1]
                        )
                    )
                    i--
                    j--
                    continue
                }

                val subCost = dp[i - 1][j - 1] + 1.2
                val delCost = dp[i - 1][j] + 1.0
                val insCost = dp[i][j - 1] + 1.0
                val minCost = dp[i][j]

                if (abs(minCost - subCost) < 1e-6) {
                    resultWords.add(
                        DiffWord(
                            kind = DiffKind.SUBSTITUTE,
                            expected = expectedWords[i - 1],
                            typed = typedWords[j - 1]
                        )
                    )
                    i--
                    j--
                    continue
                }

                if (abs(minCost - delCost) < 1e-6) {
                    resultWords.add(
                        DiffWord(
                            kind = DiffKind.MISSING,
                            expected = expectedWords[i - 1]
                        )
                    )
                    i--
                    continue
                }

                if (abs(minCost - insCost) < 1e-6) {
                    resultWords.add(
                        DiffWord(
                            kind = DiffKind.EXTRA,
                            typed = typedWords[j - 1]
                        )
                    )
                    j--
                    continue
                }
            }

            if (i > 0) {
                resultWords.add(
                    DiffWord(
                        kind = DiffKind.MISSING,
                        expected = expectedWords[i - 1]
                    )
                )
                i--
            } else if (j > 0) {
                resultWords.add(
                    DiffWord(
                        kind = DiffKind.EXTRA,
                        typed = typedWords[j - 1]
                    )
                )
                j--
            }
        }

        resultWords.reverse()

        val correctCount = resultWords.count { it.kind == DiffKind.EQUAL }
        val accuracy = if (n > 0) correctCount.toDouble() / n else 0.0
        val isPerfect = accuracy == 1.0 && resultWords.none {
            it.kind == DiffKind.SUBSTITUTE || it.kind == DiffKind.MISSING || it.kind == DiffKind.EXTRA
        }

        return DiffResult(
            words = resultWords,
            correctCount = correctCount,
            expectedCount = n,
            accuracy = accuracy,
            isPerfect = isPerfect
        )
    }
}
