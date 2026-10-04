package com.dictalearn.app.ui

import androidx.lifecycle.ViewModel
import com.dictalearn.app.domain.audio.AudioEngine
import com.dictalearn.app.domain.audio.SpeechEngine
import com.dictalearn.app.domain.diff.DiffEngine
import com.dictalearn.app.domain.diff.DiffKind
import com.dictalearn.app.domain.diff.DiffResult
import com.dictalearn.app.domain.mistakes.MistakeKind
import com.dictalearn.app.domain.mistakes.MistakeRecord
import com.dictalearn.app.domain.mistakes.MistakeRepository
import com.dictalearn.app.domain.model.Lesson
import com.dictalearn.app.domain.model.Segment
import com.dictalearn.app.domain.words.WordFeedback
import com.dictalearn.app.domain.words.WordModeEngine
import com.dictalearn.app.domain.words.WordToken
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow

enum class SessionState {
    DICTATING,
    REVIEWING,
    SHADOWING,
    COMPLETED
}

enum class StudyMode {
    SENTENCE,
    WORD
}

data class SegmentRecord(
    val segmentId: Int,
    val accuracy: Double,
    val replayCount: Int,
    val isPerfect: Boolean
)

class StudySessionViewModel(
    lesson: Lesson,
    private val audioEngine: AudioEngine,
    val mistakeRepository: MistakeRepository? = null,
    autoPlay: Boolean = true,
    val speechEngine: SpeechEngine? = null,
    initialMode: StudyMode = StudyMode.SENTENCE,
    initialSegmentIndex: Int = 0,
    initialSpeed: Float = 1.0f,
    private val onProgress: (Int) -> Unit = {},
    private val onComplete: () -> Unit = {},
    /** Result of every first attempt (e.g. to remember hard sentences). */
    private val onRecord: (SegmentRecord) -> Unit = {}
) : ViewModel() {

    /** Can grow while a PDF is still being read in the background (see extendLesson). */
    var lesson: Lesson = lesson
        private set

    private val _totalSegments = MutableStateFlow(lesson.segments.size)
    val totalSegmentsFlow: StateFlow<Int> = _totalSegments.asStateFlow()

    private val _state = MutableStateFlow(SessionState.DICTATING)
    val state: StateFlow<SessionState> = _state.asStateFlow()

    private val _studyMode = MutableStateFlow(initialMode)
    val studyMode: StateFlow<StudyMode> = _studyMode.asStateFlow()

    private val _currentSegmentIndex = MutableStateFlow(clampIndex(initialSegmentIndex))
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

    private val _speed = MutableStateFlow(initialSpeed)
    val speed: StateFlow<Float> = _speed.asStateFlow()

    private val _autoPlay = MutableStateFlow(autoPlay)
    val autoPlay: StateFlow<Boolean> = _autoPlay.asStateFlow()

    // Word Mode states
    private val _targetWords = MutableStateFlow(WordModeEngine.tokenizeSentence(currentSegment.text))
    val targetWords: StateFlow<List<WordToken>> = _targetWords.asStateFlow()

    private val _currentWordIndex = MutableStateFlow(0)
    val currentWordIndex: StateFlow<Int> = _currentWordIndex.asStateFlow()

    private val _typedWord = MutableStateFlow("")
    val typedWord: StateFlow<String> = _typedWord.asStateFlow()

    private val _wordFeedback = MutableStateFlow(WordFeedback.IDLE)
    val wordFeedback: StateFlow<WordFeedback> = _wordFeedback.asStateFlow()

    private val _autoSpeakWord = MutableStateFlow(true)
    val autoSpeakWord: StateFlow<Boolean> = _autoSpeakWord.asStateFlow()

    // Word indexes missed (wrong at least once, or skipped) in the current sentence.
    private val missedWords = mutableSetOf<Int>()

    private val _records = mutableListOf<SegmentRecord>()
    val records: List<SegmentRecord> get() = _records.toList()

    private fun addRecord(record: SegmentRecord) {
        _records.add(record)
        onRecord(record)
    }

    val currentSegment: Segment
        get() = lesson.segments.getOrElse(_currentSegmentIndex.value) { lesson.segments[0] }

    val currentWord: WordToken?
        get() = _targetWords.value.getOrNull(_currentWordIndex.value)

    val totalSegments: Int
        get() = lesson.segments.size

    init {
        audioEngine.setSpeed(initialSpeed)
        onProgress(_currentSegmentIndex.value)
        startAttempt()
    }

    private fun clampIndex(index: Int): Int = index.coerceIn(0, (lesson.segments.size - 1).coerceAtLeast(0))

    /** Plays the segment and/or speaks the first word, as configured. */
    private fun startAttempt() {
        if (_autoPlay.value) {
            playCurrentSegment()
        } else if (_studyMode.value == StudyMode.WORD && _autoSpeakWord.value) {
            // With autoplay on, speaking now would talk over the sentence audio.
            speakCurrentWord()
        }
    }

    fun setStudyMode(mode: StudyMode) {
        _studyMode.value = mode
        _currentWordIndex.value = 0
        _typedWord.value = ""
        _wordFeedback.value = WordFeedback.IDLE
        missedWords.clear()
        if (mode == StudyMode.WORD && _autoSpeakWord.value) {
            speakCurrentWord()
        }
    }

    fun toggleStudyMode() {
        setStudyMode(if (_studyMode.value == StudyMode.SENTENCE) StudyMode.WORD else StudyMode.SENTENCE)
    }

    fun toggleAutoSpeakWord() {
        _autoSpeakWord.value = !_autoSpeakWord.value
    }

    fun setAutoPlay(enabled: Boolean) {
        _autoPlay.value = enabled
    }

    fun speakCurrentWord() {
        val word = currentWord?.clean
        if (!word.isNullOrBlank()) {
            speechEngine?.speak(word)
        }
    }

    fun speakWord(word: String) {
        val clean = WordModeEngine.cleanWord(word)
        if (clean.isNotBlank()) {
            speechEngine?.speak(clean)
        }
    }

    fun giveLetterHint() {
        if (_state.value != SessionState.DICTATING || _studyMode.value != StudyMode.WORD) return
        val current = currentWord ?: return
        val clean = current.clean
        val currentTyped = _typedWord.value
        if (currentTyped.length < clean.length) {
            _typedWord.value = clean.substring(0, currentTyped.length + 1)
            _wordFeedback.value = WordFeedback.IDLE
        }
    }

    fun setTypedWord(text: String) {
        _typedWord.value = text
        if (_wordFeedback.value == WordFeedback.INCORRECT) {
            _wordFeedback.value = WordFeedback.IDLE
        }
    }

    /** Counts a word as missed once; later wrong attempts on the same word are ignored. */
    private fun markWordMissed(index: Int, kind: MistakeKind, typed: String?) {
        if (!missedWords.add(index)) return
        val target = _targetWords.value.getOrNull(index) ?: return
        mistakeRepository?.addMistakes(
            listOf(
                MistakeRecord(
                    word = target.clean,
                    kind = kind,
                    typed = typed?.takeIf { it.isNotBlank() },
                    lessonId = lesson.lessonId,
                    segmentId = currentSegment.id
                )
            )
        )
    }

    private fun advanceWord() {
        _typedWord.value = ""
        val nextIdx = _currentWordIndex.value + 1
        val total = _targetWords.value.size
        if (nextIdx < total) {
            _currentWordIndex.value = nextIdx
            if (_autoSpeakWord.value) speakCurrentWord()
            return
        }
        _diffResult.value = DiffEngine.computeWordDiff(currentSegment.text, currentSegment.text)
        addRecord(
            SegmentRecord(
                segmentId = currentSegment.id,
                accuracy = ((total - missedWords.size).toDouble() / total.coerceAtLeast(1)).coerceAtLeast(0.0),
                replayCount = _replayCount.value,
                isPerfect = missedWords.isEmpty()
            )
        )
        _state.value = SessionState.SHADOWING
    }

    fun submitWord() {
        if (_state.value != SessionState.DICTATING || _studyMode.value != StudyMode.WORD) return
        val current = currentWord ?: return
        val typed = _typedWord.value.trim()
        if (typed.isEmpty()) return

        if (WordModeEngine.checkWord(current.clean, typed)) {
            _wordFeedback.value = WordFeedback.IDLE
            advanceWord()
        } else {
            _wordFeedback.value = WordFeedback.INCORRECT
            markWordMissed(_currentWordIndex.value, MistakeKind.SUBSTITUTE, typed)
        }
    }

    fun skipWord() {
        if (_state.value != SessionState.DICTATING || _studyMode.value != StudyMode.WORD) return
        if (currentWord == null) return
        markWordMissed(_currentWordIndex.value, MistakeKind.MISSING, _typedWord.value.trim())
        _wordFeedback.value = WordFeedback.IDLE
        advanceWord()
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

        val punctuationRegex = Regex("^[^\\p{L}\\p{N}]+|[^\\p{L}\\p{N}]+$")
        val mistakesToLog = diff.words.mapNotNull { word ->
            val kind = when (word.kind) {
                DiffKind.SUBSTITUTE -> MistakeKind.SUBSTITUTE
                DiffKind.MISSING -> MistakeKind.MISSING
                else -> return@mapNotNull null
            }
            val cleaned = word.expected?.replace(punctuationRegex, "")
            if (cleaned.isNullOrBlank()) return@mapNotNull null
            MistakeRecord(
                word = cleaned,
                kind = kind,
                typed = if (kind == MistakeKind.SUBSTITUTE) word.typed else null,
                lessonId = lesson.lessonId,
                segmentId = currentSegment.id
            )
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

        addRecord(
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
        if (_state.value != SessionState.DICTATING) return

        // In word mode the words already solved count as typed.
        val typedSoFar = if (_studyMode.value == StudyMode.WORD) {
            _targetWords.value.take(_currentWordIndex.value).joinToString(" ") { it.raw }
        } else ""
        val diff = DiffEngine.computeWordDiff(currentSegment.text, typedSoFar)
        _diffResult.value = diff
        logMistakes(diff)

        addRecord(
            SegmentRecord(
                segmentId = currentSegment.id,
                accuracy = diff.accuracy,
                replayCount = _replayCount.value,
                isPerfect = false
            )
        )

        _correctionText.value = ""
        _correctionDiff.value = null
        _state.value = SessionState.REVIEWING
    }

    /** Jumps to any segment, resetting the current attempt. */
    fun goToSegment(index: Int) {
        val target = clampIndex(index)
        val changed = target != _currentSegmentIndex.value
        _currentSegmentIndex.value = target
        _typedText.value = ""
        _correctionText.value = ""
        _diffResult.value = null
        _correctionDiff.value = null
        _replayCount.value = 0
        _showTranslation.value = false
        _currentWordIndex.value = 0
        _typedWord.value = ""
        _wordFeedback.value = WordFeedback.IDLE
        missedWords.clear()
        _targetWords.value = WordModeEngine.tokenizeSentence(currentSegment.text)
        _state.value = SessionState.DICTATING
        if (changed) onProgress(target)
        startAttempt()
    }

    fun nextSegment() {
        if (_state.value != SessionState.REVIEWING && _state.value != SessionState.SHADOWING) return

        if (_currentSegmentIndex.value >= lesson.segments.size - 1) {
            audioEngine.pause()
            _state.value = SessionState.COMPLETED
            onComplete()
        } else {
            goToSegment(_currentSegmentIndex.value + 1)
        }
    }

    /** Moves forward without finishing the lesson. */
    fun skipSegment() {
        if (_currentSegmentIndex.value < lesson.segments.size - 1) {
            goToSegment(_currentSegmentIndex.value + 1)
        }
    }

    fun previousSegment() {
        if (_currentSegmentIndex.value > 0) {
            goToSegment(_currentSegmentIndex.value - 1)
        }
    }

    /**
     * Appends the new segments of a growing lesson (PDF pages read in the background). The current
     * attempt and position are kept; anything that is not a pure extension is ignored.
     */
    fun extendLesson(longer: Lesson) {
        val current = lesson.segments
        if (longer.segments.size <= current.size) return
        if (longer.segments.subList(0, current.size) != current) return
        val wasCompleted = _state.value == SessionState.COMPLETED
        lesson = longer
        _totalSegments.value = longer.segments.size
        if (wasCompleted) goToSegment(current.size)
    }

    fun restart() {
        _records.clear()
        goToSegment(0)
    }

    fun setSpeed(speed: Float) {
        _speed.value = speed
        audioEngine.setSpeed(speed)
    }

    override fun onCleared() {
        super.onCleared()
        speechEngine?.stop()
    }
}
