package com.dictalearn.app.data.download

import kotlinx.coroutines.currentCoroutineContext
import kotlinx.coroutines.ensureActive
import java.io.File
import java.io.IOException
import java.io.InputStream
import java.net.HttpURLConnection
import java.net.URL

data class DownloadItem(val url: String, val target: File)

/** [total] grows as each file's size becomes known; the first file (the audio) is by far the largest. */
data class DownloadProgress(val bytes: Long, val total: Long)

/**
 * Downloads files one after another. Each file is written to `<name>.part` and renamed only when
 * complete, so an interrupted or cancelled download never leaves a truncated file behind, and
 * files that already exist are skipped.
 */
class FileDownloader(private val open: (String) -> Source = ::openHttp) {

    class Source(val stream: InputStream, val length: Long)

    suspend fun download(items: List<DownloadItem>, onProgress: (DownloadProgress) -> Unit) {
        var done = 0L
        for (item in items) {
            if (item.target.exists()) continue
            item.target.parentFile?.mkdirs()
            val part = File(item.target.path + ".part")
            try {
                val source = open(item.url)
                val total = done + source.length
                var written = 0L
                source.stream.use { input ->
                    part.outputStream().use { output ->
                        val buffer = ByteArray(64 * 1024)
                        var lastReport = 0L
                        while (true) {
                            currentCoroutineContext().ensureActive()
                            val n = input.read(buffer)
                            if (n < 0) break
                            output.write(buffer, 0, n)
                            written += n
                            if (written - lastReport >= REPORT_EVERY) {
                                lastReport = written
                                onProgress(DownloadProgress(done + written, total))
                            }
                        }
                    }
                }
                if (source.length >= 0 && written != source.length) {
                    throw IOException("Incomplete download: $written of ${source.length} bytes (${item.url})")
                }
                if (!part.renameTo(item.target)) throw IOException("Cannot save ${item.target}")
                done += written
                onProgress(DownloadProgress(done, done))
            } finally {
                part.delete()
            }
        }
    }

    private companion object {
        const val REPORT_EVERY = 256 * 1024L

        fun openHttp(url: String): Source {
            val connection = URL(url).openConnection() as HttpURLConnection
            connection.connectTimeout = 15_000
            connection.readTimeout = 30_000
            // A gzip-encoded body would not match Content-Length; MP3/PDF gain nothing from it anyway.
            connection.setRequestProperty("Accept-Encoding", "identity")
            val code = connection.responseCode
            if (code != HttpURLConnection.HTTP_OK) {
                connection.disconnect()
                throw IOException("HTTP $code for $url")
            }
            return Source(connection.inputStream, connection.contentLengthLong)
        }
    }
}
