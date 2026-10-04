package com.dictalearn.app.data

import com.dictalearn.app.data.download.DownloadItem
import com.dictalearn.app.data.download.DownloadProgress
import com.dictalearn.app.data.download.FileDownloader
import kotlinx.coroutines.runBlocking
import org.junit.Assert.*
import org.junit.Rule
import org.junit.Test
import org.junit.rules.TemporaryFolder
import java.io.ByteArrayInputStream
import java.io.IOException
import java.io.InputStream

class FileDownloaderTest {

    @get:Rule
    val tmp = TemporaryFolder()

    private fun downloader(files: Map<String, ByteArray>, opened: MutableList<String> = mutableListOf()) =
        FileDownloader { url ->
            opened += url
            val bytes = files[url] ?: throw IOException("404 $url")
            FileDownloader.Source(ByteArrayInputStream(bytes), bytes.size.toLong())
        }

    @Test
    fun download_writesEveryFile_createsFolders_andReportsFullProgress() = runBlocking {
        val audio = ByteArray(300_000) { (it % 251).toByte() }
        val pdf = ByteArray(1_000) { 7 }
        val a = tmp.root.resolve("books/x/audio.mp3")
        val p = tmp.root.resolve("books/x/x.pdf")
        val progress = mutableListOf<DownloadProgress>()

        downloader(mapOf("u/audio" to audio, "u/pdf" to pdf))
            .download(listOf(DownloadItem("u/audio", a), DownloadItem("u/pdf", p))) { progress += it }

        assertArrayEquals(audio, a.readBytes())
        assertArrayEquals(pdf, p.readBytes())
        val last = progress.last()
        assertEquals(301_000L, last.bytes)
        assertEquals(301_000L, last.total)
        assertTrue(progress.zipWithNext().all { (x, y) -> y.bytes >= x.bytes })
    }

    @Test
    fun download_skipsFilesThatAreAlreadyThere() = runBlocking {
        val target = tmp.root.resolve("a.mp3").apply { writeText("cached") }
        val opened = mutableListOf<String>()

        downloader(emptyMap(), opened).download(listOf(DownloadItem("u/a", target))) {}

        assertTrue(opened.isEmpty())
        assertEquals("cached", target.readText())
    }

    @Test
    fun interruptedDownload_leavesNoPartialFile() {
        val target = tmp.root.resolve("books/x/audio.mp3")
        val broken = FileDownloader { _ ->
            val failing = object : InputStream() {
                var left = 50_000
                override fun read(): Int = if (left-- > 0) 1 else throw IOException("connection reset")
            }
            FileDownloader.Source(failing, 100_000)
        }

        assertThrows(IOException::class.java) {
            runBlocking { broken.download(listOf(DownloadItem("u/a", target))) {} }
        }
        assertFalse(target.exists())
        assertTrue(target.parentFile!!.listFiles().orEmpty().isEmpty())
    }

    @Test
    fun truncatedResponse_isRejected() {
        val target = tmp.root.resolve("audio.mp3")
        val short = FileDownloader { _ -> FileDownloader.Source(ByteArrayInputStream(ByteArray(10)), 20) }

        assertThrows(IOException::class.java) {
            runBlocking { short.download(listOf(DownloadItem("u/a", target))) {} }
        }
        assertFalse(target.exists())
    }
}
