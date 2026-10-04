package com.dictalearn.app.data.pdf

import android.content.Context
import android.net.Uri
import android.provider.OpenableColumns
import com.dictalearn.app.domain.progress.KeyValueStore
import org.json.JSONArray
import org.json.JSONObject
import java.io.File

data class UserPdf(val id: String, val name: String, val addedAt: Long)

/** PDFs the user added from the device; copied into app storage so they stay available. */
class UserPdfStore(private val context: Context, private val store: KeyValueStore) {
    private companion object {
        const val KEY = "user_pdfs_v1"
    }

    private val dir = File(context.filesDir, "pdfs").apply { mkdirs() }

    fun list(): List<UserPdf> {
        val raw = store.getString(KEY) ?: return emptyList()
        return runCatching {
            val arr = JSONArray(raw)
            (0 until arr.length()).map { i ->
                val o = arr.getJSONObject(i)
                UserPdf(o.getString("id"), o.getString("name"), o.optLong("addedAt"))
            }.filter { file(it.id).exists() }
        }.getOrDefault(emptyList())
    }

    fun file(id: String): File = File(dir, "$id.pdf")

    /** Copies the picked document; a file with the same name replaces the older copy. */
    fun add(uri: Uri): UserPdf {
        val name = displayName(uri) ?: "Belge.pdf"
        val pdf = UserPdf("custom_user_${System.currentTimeMillis()}", name, System.currentTimeMillis())
        context.contentResolver.openInputStream(uri)?.use { input ->
            file(pdf.id).outputStream().use { input.copyTo(it) }
        } ?: error("PDF okunamadı")
        val others = list().filter { it.name != name }
        list().filter { it.name == name }.forEach { file(it.id).delete() }
        save(listOf(pdf) + others)
        return pdf
    }

    fun remove(id: String) {
        file(id).delete()
        save(list().filter { it.id != id })
    }

    private fun save(items: List<UserPdf>) {
        val arr = JSONArray()
        items.forEach { arr.put(JSONObject().put("id", it.id).put("name", it.name).put("addedAt", it.addedAt)) }
        store.putString(KEY, arr.toString())
    }

    private fun displayName(uri: Uri): String? =
        context.contentResolver.query(uri, arrayOf(OpenableColumns.DISPLAY_NAME), null, null, null)?.use { c ->
            if (c.moveToFirst()) c.getString(0) else null
        }
}
