package com.dictalearn.app.data.download

import android.content.Context
import com.dictalearn.app.domain.library.CatalogBook
import com.dictalearn.app.domain.library.RemoteLessons
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import java.io.File

/**
 * Where a book's audio and PDF come from. The APK bundles the large files of only a few books
 * (see app/build.gradle.kts); every other book is downloaded once into filesDir/books/<id>/ and
 * then works offline like a bundled one.
 */
class BookStore(private val context: Context, private val downloader: FileDownloader = FileDownloader()) {
    private val root = File(context.filesDir, "books")

    private val bundled: Set<String> by lazy {
        context.assets.list("lessons").orEmpty().filterTo(HashSet()) { id ->
            runCatching { "audio.mp3" in context.assets.list("lessons/$id").orEmpty() }.getOrDefault(false)
        }
    }

    private fun file(book: CatalogBook, name: String) = File(root, "${book.id}/$name")

    fun isBundled(book: CatalogBook): Boolean = book.id in bundled

    /** True when the book can be studied without a connection. */
    fun isOnDevice(book: CatalogBook): Boolean =
        isBundled(book) || book.downloadFiles.all { file(book, it).exists() }

    /** Path for [com.dictalearn.app.domain.audio.AudioEngine.load]. */
    fun audioSource(book: CatalogBook): String =
        if (isBundled(book)) "assets/${book.audioAssetPath}" else file(book, "audio.mp3").path

    /** The downloaded PDF, or null when the PDF is read from the APK assets. */
    fun pdfFile(book: CatalogBook): File? =
        if (isBundled(book)) null else book.pdfAssetPath?.let { file(book, it.substringAfterLast('/')) }

    suspend fun download(book: CatalogBook, onProgress: (DownloadProgress) -> Unit) = withContext(Dispatchers.IO) {
        downloader.download(book.downloadFiles.map { DownloadItem(RemoteLessons.url(book.id, it), file(book, it)) }, onProgress)
    }

    fun remove(book: CatalogBook) {
        if (!isBundled(book)) File(root, book.id).deleteRecursively()
    }
}
