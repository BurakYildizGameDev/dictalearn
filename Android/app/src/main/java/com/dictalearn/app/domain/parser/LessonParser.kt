package com.dictalearn.app.domain.parser

import com.dictalearn.app.domain.model.Attribution
import com.dictalearn.app.domain.model.Lesson
import com.dictalearn.app.domain.model.Segment
import com.dictalearn.app.domain.model.ValidationResult
import org.json.JSONObject

object LessonParser {

    fun parse(jsonString: String): ValidationResult {
        val errors = mutableListOf<String>()

        val root = try {
            JSONObject(jsonString)
        } catch (e: Exception) {
            return ValidationResult(
                isValid = false,
                errors = listOf("Invalid JSON format: ${e.message}")
            )
        }

        val schemaVersion = root.optInt("schema_version", -1)
        if (schemaVersion != 1) {
            errors.add("Unsupported schema_version: $schemaVersion. Expected: 1")
        }

        val lessonId = root.optString("lesson_id", "").trim()
        if (lessonId.isEmpty()) {
            errors.add("Missing or invalid lesson_id. Must be a non-empty string.")
        }

        val title = root.optString("title", "").trim()
        if (title.isEmpty()) {
            errors.add("Missing or invalid title. Must be a non-empty string.")
        }

        val audioFile = root.optString("audio_file", "").trim()
        if (audioFile.isEmpty()) {
            errors.add("Missing or invalid audio_file. Must be a non-empty string.")
        }

        val sourceLang = root.optString("source_lang", "en")
        val targetLang = root.optString("target_lang", "tr")

        val attributionObj = root.optJSONObject("attribution")
        val attribution = if (attributionObj != null) {
            Attribution(
                source = attributionObj.optString("source", ""),
                license = attributionObj.optString("license", "")
            )
        } else null

        val segmentsArray = root.optJSONArray("segments")
        val segments = mutableListOf<Segment>()

        if (segmentsArray == null || segmentsArray.length() == 0) {
            errors.add("Lesson must contain a non-empty array of segments.")
        } else {
            var lastId = 0
            var lastEndMs = -1

            for (i in 0 until segmentsArray.length()) {
                val segObj = segmentsArray.optJSONObject(i)
                if (segObj == null) {
                    errors.add("Segment at index $i is invalid or null.")
                    continue
                }

                val id = segObj.optInt("id", -1)
                if (id <= lastId) {
                    errors.add("Segment at index $i has invalid id: $id. Segment IDs must be strictly ascending integers.")
                } else {
                    lastId = id
                }

                val startMs = segObj.optInt("start_ms", -1)
                val endMs = segObj.optInt("end_ms", -1)

                if (startMs < 0 || endMs < 0) {
                    errors.add("Segment $id must have positive numeric start_ms and end_ms.")
                } else {
                    if (startMs >= endMs) {
                        errors.add("Segment $id: start_ms must be less than end_ms ($startMs >= $endMs).")
                    }
                    if (startMs < lastEndMs) {
                        errors.add("Segment $id overlaps with preceding segment ($startMs < $lastEndMs).")
                    }
                    lastEndMs = endMs
                }

                val text = segObj.optString("text", "").trim()
                if (text.isEmpty()) {
                    errors.add("Segment $id: text is empty.")
                }

                val translation = segObj.optString("translation").takeIf { it.isNotBlank() }
                val notes = segObj.optString("notes").takeIf { it.isNotBlank() }

                segments.add(
                    Segment(
                        id = id,
                        startMs = startMs,
                        endMs = endMs,
                        text = text,
                        translation = translation,
                        notes = notes
                    )
                )
            }
        }

        if (errors.isNotEmpty()) {
            return ValidationResult(isValid = false, errors = errors)
        }

        return ValidationResult(
            isValid = true,
            errors = emptyList(),
            lesson = Lesson(
                schemaVersion = schemaVersion,
                lessonId = lessonId,
                title = title,
                sourceLang = sourceLang,
                targetLang = targetLang,
                audioFile = audioFile,
                attribution = attribution,
                segments = segments
            )
        )
    }

    fun toJson(lesson: Lesson): String {
        val root = JSONObject()
        root.put("schema_version", lesson.schemaVersion)
        root.put("lesson_id", lesson.lessonId)
        root.put("title", lesson.title)
        root.put("source_lang", lesson.sourceLang)
        root.put("target_lang", lesson.targetLang)
        root.put("audio_file", lesson.audioFile)

        lesson.attribution?.let {
            val attr = JSONObject()
            attr.put("source", it.source)
            attr.put("license", it.license)
            root.put("attribution", attr)
        }

        val segmentsArray = org.json.JSONArray()
        for (seg in lesson.segments) {
            val segObj = JSONObject()
            segObj.put("id", seg.id)
            segObj.put("start_ms", seg.startMs)
            segObj.put("end_ms", seg.endMs)
            segObj.put("text", seg.text)
            seg.translation?.let { segObj.put("translation", it) }
            seg.notes?.let { segObj.put("notes", it) }
            segmentsArray.put(segObj)
        }
        root.put("segments", segmentsArray)

        return root.toString(2)
    }
}
