package com.dictalearn.app.ui

import androidx.lifecycle.ViewModel
import com.dictalearn.app.domain.audio.AudioEngine
import com.dictalearn.app.domain.diff.DiffEngine
import com.dictalearn.app.domain.diff.DiffOptions
import com.dictalearn.app.domain.diff.DiffResult
import com.dictalearn.app.domain.model.Lesson
import com.dictalearn.app.domain.model.Segment
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow

enum class SessionState {
    DICTATING,
    REVIEWING,
    SHADOWING,
    COMPLETED
}

data class SegmentRecord(
    val segmentId: Int,
    val accuracy: Double,
    val replayCount: Int,
    val isPerfect: Boolean
)

class StudySessionViewModel(
    val lesson: Lesson,
    private val audioEngine: AudioEngine,
    private val autoPlay: Boolean = true
) : ViewModel() {

    private val _state = MutableStateFlow(SessionState.DICTATING)
    val state: StateFlow<SessionState> = _state.asStateFlow()

    private val _currentSegmentIndex = MutableStateFlow(0)
    val currentSegmentIndex: StateFlow<Int> = _currentSegmentIndex.asStateFlow()

    private val _typedText = MutableStateFlow("")
    val typedText: StateFlow<String> = _typedText.asStateFlow()

    private val _diffResult = MutableStateFlow<DiffResult?>(null)
    val diffResult: StateFlow<DiffResult?> = _diffResult.asStateFlow()

    private val _replayCount = MutableStateFlow(0)
    val replayCount: StateFlow<Int> = _replayCount.asStateFlow()

    private val _records = mutableListOf<SegmentRecord>()
    val records: List<SegmentRecord> get() = _records.toList()

    val currentSegment: Segment
        get() = lesson.segments.getOrElse(_currentSegmentIndex.value) { lesson.segments[0] }

    val totalSegments: Int
        get() = lesson.segments.size

    init {
        if (autoPlay) {
            playCurrentSegment()
        }
    }

    fun setTypedText(text: String) {
        _typedText.value = text
    }

    fun playCurrentSegment() {
        audioEngine.playRange(currentSegment.startMs, currentSegment.endMs)
    }

    fun replaySegment() {
        _replayCount.value += 1
        playCurrentSegment()
    }

    fun submitAnswer() {
        if (_state.value != SessionState.DICTATING) return

        val text = _typedText.value.trim()
        if (text.isEmpty()) return

        val diff = DiffEngine.computeWordDiff(currentSegment.text, text)
        _diffResult.value = diff
        _state.value = SessionState.REVIEWING

        _records.add(
            SegmentRecord(
                segmentId = currentSegment.id,
                accuracy = diff.accuracy,
                replayCount = _replayCount.value,
                isPerfect = diff.isPerfect
            )
        )
    }

    fun giveUp() {
        if (_state.value != SessionState.DICTATING && _state.value != SessionState.REVIEWING) return

        val diff = DiffEngine.computeWordDiff(currentSegment.text, "")
        _diffResult.value = diff
        _state.value = SessionState.REVIEWING

        _records.add(
            SegmentRecord(
                segmentId = currentSegment.id,
                accuracy = 0.0,
                replayCount = _replayCount.value,
                isPerfect = false
            )
        )
    }

    fun nextSegment() {
        if (_state.value != SessionState.REVIEWING && _state.value != SessionState.SHADOWING) return

        val isLast = _currentSegmentIndex.value >= lesson.segments.size - 1
        if (isLast) {
            _state.value = SessionState.COMPLETED
        } else {
            _currentSegmentIndex.value += 1
            _typedText.value = ""
            _diffResult.value = null
            _replayCount.value = 0
            _state.value = SessionState.DICTATING

            if (autoPlay) {
                playCurrentSegment()
            }
        }
    }

    fun setSpeed(speed: Float) {
        audioEngine.setSpeed(speed)
    }
}
