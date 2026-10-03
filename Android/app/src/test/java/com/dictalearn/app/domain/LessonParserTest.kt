package com.dictalearn.app.domain

import com.dictalearn.app.domain.parser.LessonParser
import org.junit.Assert.*
import org.junit.Test

class LessonParserTest {

    private val validJson = """
        {
          "schema_version": 1,
          "lesson_id": "sample_ch01",
          "title": "Chapter 1: The Departure",
          "source_lang": "en",
          "target_lang": "tr",
          "audio_file": "audio.wav",
          "attribution": {
            "source": "LibriVox",
            "license": "Public Domain"
          },
          "segments": [
            {
              "id": 1,
              "start_ms": 0,
              "end_ms": 4000,
              "text": "He packed his small brown suitcase.",
              "translation": "Küçük bavulunu topladı.",
              "notes": "packed: düzenli fiil"
            },
            {
              "id": 2,
              "start_ms": 4500,
              "end_ms": 7500,
              "text": "The morning cold hit him immediately.",
              "translation": "Sabahın soğuğu anında yüzüne çarptı."
            }
          ]
        }
    """.trimIndent()

    @Test
    fun parse_validLesson_returnsValidResult() {
        val result = LessonParser.parse(validJson)
        assertTrue(result.isValid)
        assertTrue(result.errors.isEmpty())
        assertNotNull(result.lesson)
        assertEquals("sample_ch01", result.lesson?.lessonId)
        assertEquals(2, result.lesson?.segments?.size)
    }

    @Test
    fun parse_unsupportedSchemaVersion_fails() {
        val json = validJson.replace("\"schema_version\": 1", "\"schema_version\": 2")
        val result = LessonParser.parse(json)
        assertFalse(result.isValid)
        assertTrue(result.errors.any { it.contains("Unsupported schema_version") })
    }

    @Test
    fun parse_emptySegments_fails() {
        val json = """{"schema_version": 1, "lesson_id": "test", "title": "T", "audio_file": "a.wav", "segments": []}"""
        val result = LessonParser.parse(json)
        assertFalse(result.isValid)
        assertTrue(result.errors.any { it.contains("non-empty array of segments") })
    }

    @Test
    fun parse_unorderedSegmentIds_fails() {
        val json = """
            {
              "schema_version": 1,
              "lesson_id": "test",
              "title": "T",
              "audio_file": "a.wav",
              "segments": [
                {"id": 2, "start_ms": 0, "end_ms": 1000, "text": "First"},
                {"id": 1, "start_ms": 1200, "end_ms": 2000, "text": "Second"}
              ]
            }
        """.trimIndent()
        val result = LessonParser.parse(json)
        assertFalse(result.isValid)
        assertTrue(result.errors.any { it.contains("strictly ascending") })
    }

    @Test
    fun parse_overlappingSegments_fails() {
        val json = """
            {
              "schema_version": 1,
              "lesson_id": "test",
              "title": "T",
              "audio_file": "a.wav",
              "segments": [
                {"id": 1, "start_ms": 0, "end_ms": 3000, "text": "First"},
                {"id": 2, "start_ms": 2500, "end_ms": 5000, "text": "Second"}
              ]
            }
        """.trimIndent()
        val result = LessonParser.parse(json)
        assertFalse(result.isValid)
        assertTrue(result.errors.any { it.contains("overlaps") })
    }
}
