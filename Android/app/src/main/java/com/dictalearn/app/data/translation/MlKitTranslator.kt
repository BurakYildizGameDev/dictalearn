package com.dictalearn.app.data.translation

import com.dictalearn.app.domain.translation.SentenceTranslator
import com.google.mlkit.common.model.DownloadConditions
import com.google.mlkit.nl.translate.TranslateLanguage
import com.google.mlkit.nl.translate.Translation
import com.google.mlkit.nl.translate.TranslatorOptions
import kotlinx.coroutines.tasks.await

/**
 * Google ML Kit on-device EN -> TR translation (Faz 7.1). The language model (~30 MB) is
 * downloaded once on first use; afterwards translation works fully offline.
 */
class MlKitTranslator : SentenceTranslator {
    private val client = Translation.getClient(
        TranslatorOptions.Builder()
            .setSourceLanguage(TranslateLanguage.ENGLISH)
            .setTargetLanguage(TranslateLanguage.TURKISH)
            .build()
    )

    @Volatile
    private var modelReady = false

    override suspend fun translate(text: String): Result<String> = runCatching {
        if (!modelReady) {
            client.downloadModelIfNeeded(DownloadConditions.Builder().build()).await()
            modelReady = true
        }
        client.translate(text).await()
    }

    override fun close() {
        client.close()
    }
}
