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

/**
 * Plays millisecond ranges of a lesson file with MediaPlayer.
 *
 * - Preparation is asynchronous (no main-thread blocking on long books); a range requested
 *   while loading is played as soon as the player is ready.
 * - Seeks use SEEK_CLOSEST (API 26+) so a range starts on the exact millisecond.
 * - The range end is detected by polling the playback position, so speed changes during
 *   playback can't cut the sentence early or let it run over.
 */
class MediaPlayerAudioEngine(private val context: Context) : AudioEngine {
    private var mediaPlayer: MediaPlayer? = null
    private var prepared = false
    private val _status = MutableStateFlow(AudioStatus.IDLE)
    override val status: StateFlow<AudioStatus> = _status.asStateFlow()

    private var currentSpeed: Float = 1.0f
    private val scope = CoroutineScope(Dispatchers.Main + SupervisorJob())
    private var watchJob: Job? = null
    private var pendingRange: Pair<Int, Int>? = null
    private var rangeEndMs: Int = 0

    override fun load(path: String) {
        watchJob?.cancel()
        pendingRange = null
        prepared = false
        mediaPlayer?.release()
        _status.value = AudioStatus.LOADING

        try {
            mediaPlayer = MediaPlayer().apply {
                when {
                    path.startsWith("assets/") -> {
                        context.assets.openFd(path.removePrefix("assets/")).use { afd ->
                            setDataSource(afd.fileDescriptor, afd.startOffset, afd.length)
                        }
                    }
                    File(path).exists() -> setDataSource(path)
                    else -> setDataSource(context, android.net.Uri.parse(path))
                }
                setOnPreparedListener {
                    prepared = true
                    _status.value = AudioStatus.IDLE
                    pendingRange?.let { (start, end) ->
                        pendingRange = null
                        playRange(start, end)
                    }
                }
                setOnErrorListener { _, _, _ ->
                    _status.value = AudioStatus.ERROR
                    true
                }
                prepareAsync()
            }
        } catch (e: Exception) {
            _status.value = AudioStatus.ERROR
        }
    }

    override fun playRange(startMs: Int, endMs: Int) {
        val player = mediaPlayer ?: return
        if (!prepared) {
            pendingRange = startMs to endMs
            return
        }
        watchJob?.cancel()
        rangeEndMs = endMs

        try {
            if (player.isPlaying) player.pause()
            player.setOnSeekCompleteListener {
                it.setOnSeekCompleteListener(null)
                startPlayback(it)
            }
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
                player.seekTo(startMs.toLong(), MediaPlayer.SEEK_CLOSEST)
            } else {
                player.seekTo(startMs)
            }
            _status.value = AudioStatus.PLAYING
        } catch (e: Exception) {
            _status.value = AudioStatus.ERROR
        }
    }

    private fun startPlayback(player: MediaPlayer) {
        try {
            player.start()
            // Speed must be applied after start(): on a paused player setPlaybackParams is ignored
            // on some devices and starts playback on others.
            applySpeed()
            _status.value = AudioStatus.PLAYING
            watchRangeEnd(player)
        } catch (e: Exception) {
            _status.value = AudioStatus.ERROR
        }
    }

    private fun watchRangeEnd(player: MediaPlayer) {
        watchJob?.cancel()
        watchJob = scope.launch {
            while (isActive) {
                val position = try {
                    player.currentPosition
                } catch (_: IllegalStateException) {
                    break
                }
                if (position >= rangeEndMs || !player.isPlaying) break
                delay(15)
            }
            if (player.isPlaying) player.pause()
            if (_status.value == AudioStatus.PLAYING) {
                _status.value = AudioStatus.RANGE_COMPLETED
            }
        }
    }

    override fun pause() {
        watchJob?.cancel()
        pendingRange = null
        mediaPlayer?.let {
            if (it.isPlaying) {
                it.pause()
                _status.value = AudioStatus.PAUSED
            } else if (_status.value == AudioStatus.PLAYING) {
                // Paused while still seeking: don't start once the seek completes.
                it.setOnSeekCompleteListener(null)
                _status.value = AudioStatus.PAUSED
            }
        }
    }

    override fun resume() {
        val player = mediaPlayer ?: return
        // Only a paused range can continue; never play past the end of the sentence.
        if (_status.value != AudioStatus.PAUSED || !prepared) return
        startPlayback(player)
    }

    override fun setSpeed(speed: Float) {
        currentSpeed = speed.coerceIn(0.25f, 2.5f)
        applySpeed()
    }

    override fun getSpeed(): Float = currentSpeed

    private fun applySpeed() {
        val player = mediaPlayer ?: return
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M && prepared && player.isPlaying) {
            try {
                player.playbackParams = player.playbackParams.setSpeed(currentSpeed)
            } catch (_: Exception) {
            }
        }
    }

    override fun dispose() {
        watchJob?.cancel()
        scope.cancel()
        mediaPlayer?.release()
        mediaPlayer = null
        prepared = false
        _status.value = AudioStatus.IDLE
    }
}
