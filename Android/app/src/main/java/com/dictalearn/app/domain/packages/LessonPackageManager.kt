package com.dictalearn.app.domain.packages

import com.dictalearn.app.domain.model.Lesson
import com.dictalearn.app.domain.parser.LessonParser
import java.io.ByteArrayInputStream
import java.io.ByteArrayOutputStream
import java.util.zip.ZipEntry
import java.util.zip.ZipInputStream
import java.util.zip.ZipOutputStream

data class ImportedPackage(
    val lesson: Lesson,
    val audioBytes: ByteArray,
    val audioFileName: String
)

object LessonPackageManager {

    fun exportPackage(lesson: Lesson, audioBytes: ByteArray): ByteArray {
        val byteOut = ByteArrayOutputStream()
        val zipOut = ZipOutputStream(byteOut)

        val jsonEntry = ZipEntry("lesson.json")
        zipOut.putNextEntry(jsonEntry)
        val jsonStr = LessonParser.toJson(lesson)
        zipOut.write(jsonStr.toByteArray(Charsets.UTF_8))
        zipOut.closeEntry()

        val audioName = lesson.audioFile.ifBlank { "audio.wav" }
        val audioEntry = ZipEntry(audioName)
        zipOut.putNextEntry(audioEntry)
        zipOut.write(audioBytes)
        zipOut.closeEntry()

        zipOut.finish()
        return byteOut.toByteArray()
    }

    fun importPackage(zipBytes: ByteArray): ImportedPackage {
        val zipIn = ZipInputStream(ByteArrayInputStream(zipBytes))
        var entry: ZipEntry? = zipIn.nextEntry

        val entries = mutableMapOf<String, ByteArray>()

        while (entry != null) {
            if (!entry.isDirectory) {
                val name = entry.name.replace('\\', '/')
                val content = zipIn.readBytes()
                entries[name] = content
            }
            zipIn.closeEntry()
            entry = zipIn.nextEntry
        }

        // Find lesson.json
        val jsonEntryName = entries.keys.find { it.endsWith("lesson.json", ignoreCase = true) }
            ?: throw IllegalArgumentException("Zip paketi içinde 'lesson.json' bulunamadı.")

        val lessonJson = entries[jsonEntryName]?.toString(Charsets.UTF_8)
            ?: throw IllegalArgumentException("'lesson.json' içeriği okunamadı.")

        val validation = LessonParser.parse(lessonJson)
        if (!validation.isValid || validation.lesson == null) {
            throw IllegalArgumentException("Geçersiz ders paketi: ${validation.errors.joinToString(", ")}")
        }

        val lesson = validation.lesson

        // Find audio
        val expectedAudio = lesson.audioFile.substringAfterLast('/')
        val foundAudioEntry = entries.keys.find { it.endsWith(expectedAudio, ignoreCase = true) }
            ?: entries.keys.find { it.matches(Regex(""".*\.(wav|mp3|m4a|ogg|aac)$""", RegexOption.IGNORE_CASE)) }
            ?: throw IllegalArgumentException("Zip paketi içinde ses dosyası bulunamadı.")

        val audioBytes = entries[foundAudioEntry]
            ?: throw IllegalArgumentException("Ses dosyası okunamadı.")
        val audioName = foundAudioEntry.substringAfterLast('/')

        return ImportedPackage(
            lesson = lesson,
            audioBytes = audioBytes,
            audioFileName = audioName
        )
    }
}
