package com.dictalearn.app.domain.model

data class Segment(
    val id: Int,
    val startMs: Int,
    val endMs: Int,
    val text: String,
    val translation: String? = null,
    val notes: String? = null
)

data class Attribution(
    val source: String,
    val license: String
)

data class Lesson(
    val schemaVersion: Int,
    val lessonId: String,
    val title: String,
    val sourceLang: String,
    val targetLang: String,
    val audioFile: String,
    val attribution: Attribution? = null,
    val segments: List<Segment>
)

data class ValidationResult(
    val isValid: Boolean,
    val errors: List<String>,
    val lesson: Lesson? = null
)
