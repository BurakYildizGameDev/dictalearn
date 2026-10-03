package com.dictalearn.app.domain.audio

import kotlinx.coroutines.flow.StateFlow

enum class AudioStatus {
    IDLE,
    LOADING,
    PLAYING,
    PAUSED,
    RANGE_COMPLETED,
    ERROR
}

interface AudioEngine {
    fun load(path: String)
    fun playRange(startMs: Int, endMs: Int)
    fun pause()
    fun resume()
    fun setSpeed(speed: Float)
    fun getSpeed(): Float
    val status: StateFlow<AudioStatus>
    fun dispose()
}
