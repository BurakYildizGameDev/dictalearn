package com.dictalearn.app.domain

import com.dictalearn.app.domain.library.LessonCatalog
import com.dictalearn.app.domain.library.RemoteLessons
import org.junit.Assert.*
import org.junit.Test

class RemoteLessonsTest {

    @Test
    fun bookFiles_areAudioAndPdf_demoHasNoPdf() {
        assertEquals(
            listOf("audio.mp3", "book_32_dracula.pdf"),
            LessonCatalog.find("book_32_dracula")!!.downloadFiles
        )
        assertEquals(listOf("audio.mp3"), LessonCatalog.find("sample_ch01")!!.downloadFiles)
    }

    @Test
    fun urls_pointToTheWebCopyOnGitHubPages() {
        assertEquals(
            "https://burakyildizgamedev.github.io/dictalearn/lessons/book_32_dracula/audio.mp3",
            RemoteLessons.url("book_32_dracula", "audio.mp3")
        )
        assertEquals(
            "https://burakyildizgamedev.github.io/dictalearn/lessons/word_audio/q.mp3",
            RemoteLessons.wordAudioUrl('q')
        )
    }
}
