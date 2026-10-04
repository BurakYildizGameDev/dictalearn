package com.dictalearn.app.data.audio

import android.content.Context
import android.speech.tts.TextToSpeech
import android.speech.tts.UtteranceProgressListener
import com.dictalearn.app.domain.audio.AudioEngine
import com.dictalearn.app.domain.audio.AudioStatus
import com.dictalearn.app.domain.model.Segment
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import java.util.Locale

/**
 * AudioEngine for lessons without an audio file (built from the user's PDFs): playRange(start_ms)
 * finds the sentence by its synthetic start time and speaks it with the system TextToSpeech.
 */
class TtsSegmentAudioEngine(context: Context) : AudioEngine {
    private val _status = MutableStateFlow(AudioStatus.IDLE)
    override val status: StateFlow<AudioStatus> = _status.asStateFlow()

    private var byStart: Map<Int, Segment> = emptyMap()
    private var speed = 1.0f
    private var ready = false
    private var pending: Int? = null
    private var currentId: String? = null
    private var lastStart: Int? = null
    private var counter = 0

    private val tts: TextToSpeech = TextToSpeech(context.applicationContext) { result ->
        if (result == TextToSpeech.SUCCESS) {
            ready = true
            pending?.let { pending = null; playRange(it, it) }
        }
    }

    init {
        tts.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
            override fun onStart(utteranceId: String?) {}
            override fun onDone(utteranceId: String?) {
                if (utteranceId == currentId && _status.value == AudioStatus.PLAYING) {
                    _status.value = AudioStatus.RANGE_COMPLETED
                }
            }
            @Deprecated("Deprecated in Java")
            override fun onError(utteranceId: String?) {
                if (utteranceId == currentId) _status.value = AudioStatus.ERROR
            }
        })
    }

    fun setSegments(segments: List<Segment>) {
        byStart = segments.associateBy { it.startMs }
    }

    override fun load(path: String) {
        _status.value = AudioStatus.IDLE
    }

    override fun playRange(startMs: Int, endMs: Int) {
        val segment = byStart[startMs] ?: return
        lastStart = startMs
        if (!ready) {
            pending = startMs
            return
        }
        tts.language = Locale.US
        tts.setSpeechRate(0.95f * speed)
        val id = "seg_${startMs}_${counter++}"
        currentId = id
        _status.value = AudioStatus.PLAYING
        tts.speak(segment.text, TextToSpeech.QUEUE_FLUSH, null, id)
    }

    override fun pause() {
        if (_status.value != AudioStatus.PLAYING) return
        currentId = null
        tts.stop()
        _status.value = AudioStatus.PAUSED
    }

    /** Speech cannot continue mid-sentence; the sentence starts over. */
    override fun resume() {
        if (_status.value == AudioStatus.PAUSED) lastStart?.let { playRange(it, it) }
    }

    override fun setSpeed(speed: Float) {
        this.speed = speed.coerceIn(0.5f, 2f)
    }

    override fun getSpeed(): Float = speed

    override fun dispose() {
        tts.stop()
        tts.shutdown()
        _status.value = AudioStatus.IDLE
    }
}
