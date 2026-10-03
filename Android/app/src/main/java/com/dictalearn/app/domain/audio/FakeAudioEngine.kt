package com.dictalearn.app.domain.audio

import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow

class FakeAudioEngine : AudioEngine {
    private val _status = MutableStateFlow(AudioStatus.IDLE)
    override val status: StateFlow<AudioStatus> = _status.asStateFlow()

    private var currentSpeed: Float = 1.0f
    var lastStartMs: Int? = null
    var lastEndMs: Int? = null
    var playCount: Int = 0

    override fun load(path: String) {
        _status.value = AudioStatus.IDLE
    }

    override fun playRange(startMs: Int, endMs: Int) {
        lastStartMs = startMs
        lastEndMs = endMs
        playCount++
        _status.value = AudioStatus.PLAYING
    }

    fun completeRange() {
        _status.value = AudioStatus.RANGE_COMPLETED
    }

    override fun pause() {
        _status.value = AudioStatus.PAUSED
    }

    override fun resume() {
        _status.value = AudioStatus.PLAYING
    }

    override fun setSpeed(speed: Float) {
        currentSpeed = speed
    }

    override fun getSpeed(): Float = currentSpeed

    override fun dispose() {
        _status.value = AudioStatus.IDLE
    }
}
