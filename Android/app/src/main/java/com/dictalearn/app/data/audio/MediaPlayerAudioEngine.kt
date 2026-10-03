package com.dictalearn.app.data.audio

import android.content.Context
import android.media.MediaPlayer
import android.os.Build
import com.dictalearn.app.domain.audio.AudioEngine
import com.dictalearn.app.domain.audio.AudioStatus
import kotlinx.coroutines.*
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import java.io.File

class MediaPlayerAudioEngine(private val context: Context) : AudioEngine {
    private var mediaPlayer: MediaPlayer? = null
    private val _status = MutableStateFlow(AudioStatus.IDLE)
    override val status: StateFlow<AudioStatus> = _status.asStateFlow()

    private var currentSpeed: Float = 1.0f
    private val scope = CoroutineScope(Dispatchers.Main + SupervisorJob())
    private var stopJob: Job? = null

    override fun load(path: String) {
        _status.value = AudioStatus.LOADING
        try {
            mediaPlayer?.release()
            mediaPlayer = MediaPlayer().apply {
                if (path.startsWith("assets/")) {
                    val afd = context.assets.openFd(path.removePrefix("assets/"))
                    setDataSource(afd.fileDescriptor, afd.startOffset, afd.length)
                    afd.close()
                } else if (File(path).exists()) {
                    setDataSource(path)
                } else {
                    setDataSource(context, android.net.Uri.parse(path))
                }
                prepare()
            }
            _status.value = AudioStatus.IDLE
        } catch (e: Exception) {
            _status.value = AudioStatus.ERROR
        }
    }

    override fun playRange(startMs: Int, endMs: Int) {
        val player = mediaPlayer ?: return
        stopJob?.cancel()

        try {
            player.seekTo(startMs)
            applySpeed()
            player.start()
            _status.value = AudioStatus.PLAYING

            val durationMs = ((endMs - startMs) / currentSpeed).toLong()
            stopJob = scope.launch {
                delay(durationMs)
                if (player.isPlaying) {
                    player.pause()
                }
                _status.value = AudioStatus.RANGE_COMPLETED
            }
        } catch (e: Exception) {
            _status.value = AudioStatus.ERROR
        }
    }

    override fun pause() {
        stopJob?.cancel()
        mediaPlayer?.let {
            if (it.isPlaying) {
                it.pause()
                _status.value = AudioStatus.PAUSED
            }
        }
    }

    override fun resume() {
        mediaPlayer?.let {
            it.start()
            _status.value = AudioStatus.PLAYING
        }
    }

    override fun setSpeed(speed: Float) {
        currentSpeed = speed.coerceIn(0.25f, 2.5f)
        applySpeed()
    }

    override fun getSpeed(): Float = currentSpeed

    private fun applySpeed() {
        val player = mediaPlayer ?: return
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M && player.isPlaying) {
            try {
                player.playbackParams = player.playbackParams.setSpeed(currentSpeed)
            } catch (_: Exception) {}
        }
    }

    override fun dispose() {
        stopJob?.cancel()
        scope.cancel()
        mediaPlayer?.release()
        mediaPlayer = null
        _status.value = AudioStatus.IDLE
    }
}
