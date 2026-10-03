package com.dictalearn.app.domain.diff

enum class DiffKind {
    EQUAL,
    SUBSTITUTE,
    MISSING,
    EXTRA
}

data class DiffWord(
    val kind: DiffKind,
    val expected: String? = null,
    val typed: String? = null
)

data class DiffOptions(
    val ignoreCase: Boolean = true,
    val ignorePunctuation: Boolean = true
)

data class DiffResult(
    val words: List<DiffWord>,
    val correctCount: Int,
    val expectedCount: Int,
    val accuracy: Double,
    val isPerfect: Boolean
)
