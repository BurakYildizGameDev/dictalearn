package com.dictalearn.app.ui

import androidx.lifecycle.ViewModel
import com.dictalearn.app.domain.audio.AudioEngine
import com.dictalearn.app.domain.diff.DiffEngine
import com.dictalearn.app.domain.diff.DiffKind
import com.dictalearn.app.domain.diff.DiffResult
import com.dictalearn.app.domain.mistakes.MistakeKind
import com.dictalearn.app.domain.mistakes.MistakeRecord
import com.dictalearn.app.domain.mistakes.MistakeRepository
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
    val mistakeRepository: MistakeRepository? = null,
    private val autoPlay: Boolean = true
) : ViewModel() {

    private val _state = MutableStateFlow(SessionState.DICTATING)
    val state: StateFlow<SessionState> = _state.asStateFlow()

    private val _currentSegmentIndex = MutableStateFlow(0)
    val currentSegmentIndex: StateFlow<Int> = _currentSegmentIndex.asStateFlow()

    private val _typedText = MutableStateFlow("")
    val typedText: StateFlow<String> = _typedText.asStateFlow()

    private val _correctionText = MutableStateFlow("")
    val correctionText: StateFlow<String> = _correctionText.asStateFlow()

    private val _diffResult = MutableStateFlow<DiffResult?>(null)
    val diffResult: StateFlow<DiffResult?> = _diffResult.asStateFlow()

    private val _correctionDiff = MutableStateFlow<DiffResult?>(null)
    val correctionDiff: StateFlow<DiffResult?> = _correctionDiff.asStateFlow()

    private val _replayCount = MutableStateFlow(0)
    val replayCount: StateFlow<Int> = _replayCount.asStateFlow()

    private val _showTranslation = MutableStateFlow(false)
    val showTranslation: StateFlow<Boolean> = _showTranslation.asStateFlow()

    private val _speed = MutableStateFlow(1.0f)
    val speed: StateFlow<Float> = _speed.asStateFlow()

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

    fun setCorrectionText(text: String) {
        _correctionText.value = text
    }

    fun playCurrentSegment() {
        audioEngine.playRange(currentSegment.startMs, currentSegment.endMs)
    }

    fun replaySegment() {
        _replayCount.value += 1
        playCurrentSegment()
    }

    fun toggleTranslation() {
        _showTranslation.value = !_showTranslation.value
    }

    private fun logMistakes(diff: DiffResult) {
        val repo = mistakeRepository ?: return
        if (diff.isPerfect) return

        val mistakesToLog = mutableListOf<MistakeRecord>()
        val punctuationRegex = Regex("^[^\\p{L}\\p{N}]+|[^\\p{L}\\p{N}]+$")

        for (word in diff.words) {
            if (word.kind == DiffKind.SUBSTITUTE && word.expected != null) {
                val cleaned = word.expected.replace(punctuationRegex, "")
                if (cleaned.isNotBlank()) {
                    mistakesToLog.add(
                        MistakeRecord(
                            word = cleaned,
                            kind = MistakeKind.SUBSTITUTE,
                            typed = word.typed,
                            lessonId = lesson.lessonId,
                            segmentId = currentSegment.id
                        )
                    )
                }
            } else if (word.kind == DiffKind.MISSING && word.expected != null) {
                val cleaned = word.expected.replace(punctuationRegex, "")
                if (cleaned.isNotBlank()) {
                    mistakesToLog.add(
                        MistakeRecord(
                            word = cleaned,
                            kind = MistakeKind.MISSING,
                            lessonId = lesson.lessonId,
                            segmentId = currentSegment.id
                        )
                    )
                }
            }
        }

        if (mistakesToLog.isNotEmpty()) {
            repo.addMistakes(mistakesToLog)
        }
    }

    fun submitAnswer() {
        if (_state.value != SessionState.DICTATING) return

        val text = _typedText.value.trim()
        if (text.isEmpty()) return

        val diff = DiffEngine.computeWordDiff(currentSegment.text, text)
        _diffResult.value = diff
        logMistakes(diff)

        _records.add(
            SegmentRecord(
                segmentId = currentSegment.id,
                accuracy = diff.accuracy,
                replayCount = _replayCount.value,
                isPerfect = diff.isPerfect
            )
        )

        if (diff.isPerfect) {
            _state.value = SessionState.SHADOWING
        } else {
            _correctionText.value = ""
            _correctionDiff.value = null
            _state.value = SessionState.REVIEWING
        }
    }

    fun submitCorrection() {
        if (_state.value != SessionState.REVIEWING) return

        val text = _correctionText.value.trim()
        if (text.isEmpty()) return

        val diff = DiffEngine.computeWordDiff(currentSegment.text, text)
        _correctionDiff.value = diff

        if (diff.isPerfect) {
            _state.value = SessionState.SHADOWING
        }
    }

    fun skipCorrection() {
        if (_state.value == SessionState.REVIEWING) {
            _state.value = SessionState.SHADOWING
        }
    }

    fun giveUp() {
        if (_state.value != SessionState.DICTATING && _state.value != SessionState.REVIEWING) return

        val diff = DiffEngine.computeWordDiff(currentSegment.text, "")
        _diffResult.value = diff
        logMistakes(diff)

        _records.add(
            SegmentRecord(
                segmentId = currentSegment.id,
                accuracy = 0.0,
                replayCount = _replayCount.value,
                isPerfect = false
            )
        )

        _correctionText.value = ""
        _correctionDiff.value = null
        _state.value = SessionState.REVIEWING
    }

    fun nextSegment() {
        if (_state.value != SessionState.REVIEWING && _state.value != SessionState.SHADOWING) return

        val isLast = _currentSegmentIndex.value >= lesson.segments.size - 1
        if (isLast) {
            _state.value = SessionState.COMPLETED
        } else {
            _currentSegmentIndex.value += 1
            _typedText.value = ""
            _correctionText.value = ""
            _diffResult.value = null
            _correctionDiff.value = null
            _replayCount.value = 0
            _showTranslation.value = false
            _state.value = SessionState.DICTATING

            if (autoPlay) {
                playCurrentSegment()
            }
        }
    }

    fun setSpeed(speed: Float) {
        _speed.value = speed
        audioEngine.setSpeed(speed)
    }
}
