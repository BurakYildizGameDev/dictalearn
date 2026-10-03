package com.dictalearn.app.domain

import com.dictalearn.app.domain.model.Lesson
import com.dictalearn.app.domain.model.Segment
import com.dictalearn.app.domain.packages.LessonPackageManager
import org.junit.Assert.*
import org.junit.Test

class LessonPackageTest {

    private val dummyLesson = Lesson(
        schemaVersion = 1,
        lessonId = "android_pack",
        title = "Android Package Test",
        sourceLang = "en",
        targetLang = "tr",
        audioFile = "audio.wav",
        segments = listOf(
            Segment(id = 1, startMs = 0, endMs = 3000, text = "He packed his suitcase.")
        )
    )

    @Test
    fun exportAndImportPackage_roundtripsSuccessfully() {
        val fakeAudioBytes = "RIFF wave mock audio bytes".toByteArray(Charsets.UTF_8)

        val zipBytes = LessonPackageManager.exportPackage(dummyLesson, fakeAudioBytes)
        assertNotNull(zipBytes)
        assertTrue(zipBytes.isNotEmpty())

        val imported = LessonPackageManager.importPackage(zipBytes)
        assertEquals("android_pack", imported.lesson.lessonId)
        assertEquals("Android Package Test", imported.lesson.title)
        assertEquals(1, imported.lesson.segments.size)
        assertEquals("He packed his suitcase.", imported.lesson.segments[0].text)
        assertEquals("audio.wav", imported.audioFileName)
        assertArrayEquals(fakeAudioBytes, imported.audioBytes)
    }

    @Test(expected = IllegalArgumentException::class)
    fun importPackage_throwsWhenNoLessonJson() {
        val emptyZip = java.io.ByteArrayOutputStream().apply {
            java.util.zip.ZipOutputStream(this).use { zipOut ->
                zipOut.putNextEntry(java.util.zip.ZipEntry("readme.txt"))
                zipOut.write("hello".toByteArray())
                zipOut.closeEntry()
            }
        }.toByteArray()

        LessonPackageManager.importPackage(emptyZip)
    }
}
