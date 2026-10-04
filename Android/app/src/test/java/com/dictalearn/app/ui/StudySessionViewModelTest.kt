package com.dictalearn.app.ui

import com.dictalearn.app.data.mistakes.InMemoryMistakeRepository
import com.dictalearn.app.domain.audio.FakeAudioEngine
import com.dictalearn.app.domain.mistakes.MistakeKind
import com.dictalearn.app.domain.model.Lesson
import com.dictalearn.app.domain.model.Segment
import org.junit.Assert.*
import org.junit.Before
import org.junit.Test

class StudySessionViewModelTest {

    private lateinit var lesson: Lesson
    private lateinit var fakeAudioEngine: FakeAudioEngine
    private lateinit var mistakeRepo: InMemoryMistakeRepository
    private lateinit var viewModel: StudySessionViewModel

    @Before
    fun setUp() {
        lesson = Lesson(
            schemaVersion = 1,
            lessonId = "test",
            title = "Test Lesson",
            sourceLang = "en",
            targetLang = "tr",
            audioFile = "audio.wav",
            segments = listOf(
                Segment(id = 1, startMs = 0, endMs = 3000, text = "He packed his suitcase."),
                Segment(id = 2, startMs = 3500, endMs = 6000, text = "The morning cold hit him.")
            )
        )
        fakeAudioEngine = FakeAudioEngine()
        mistakeRepo = InMemoryMistakeRepository()
        viewModel = StudySessionViewModel(
            lesson = lesson,
            audioEngine = fakeAudioEngine,
            mistakeRepository = mistakeRepo,
            autoPlay = true
        )
    }

    @Test
    fun initialState_isDictating_andPlaysAudio() {
        assertEquals(SessionState.DICTATING, viewModel.state.value)
        assertEquals(0, viewModel.currentSegmentIndex.value)
        assertEquals(1, fakeAudioEngine.playCount)
        assertEquals(0, fakeAudioEngine.lastStartMs)
        assertEquals(3000, fakeAudioEngine.lastEndMs)
    }

    @Test
    fun submitPerfectAnswer_transitionsDirectlyToShadowing() {
        viewModel.setTypedText("he packed his suitcase")
        viewModel.submitAnswer()

        assertEquals(SessionState.SHADOWING, viewModel.state.value)
        val diff = viewModel.diffResult.value
        assertNotNull(diff)
        assertTrue(diff!!.isPerfect)
        assertTrue(mistakeRepo.getMistakes().isEmpty())
    }

    @Test
    fun submitImperfectAnswer_transitionsToReviewing_andLogsMistakes() {
        viewModel.setTypedText("he suitcase") // missing packed, his
        viewModel.submitAnswer()

        assertEquals(SessionState.REVIEWING, viewModel.state.value)
        val diff = viewModel.diffResult.value
        assertNotNull(diff)
        assertFalse(diff!!.isPerfect)

        val mistakes = mistakeRepo.getMistakes()
        assertTrue(mistakes.isNotEmpty())
        assertTrue(mistakes.any { it.word == "packed" && it.kind == MistakeKind.MISSING })
    }

    @Test
    fun correctionFlow_advancesToShadowingWhenCorrect() {
        viewModel.setTypedText("he suitcase")
        viewModel.submitAnswer()
        assertEquals(SessionState.REVIEWING, viewModel.state.value)

        // Wrong correction attempt
        viewModel.setCorrectionText("he his suitcase")
        viewModel.submitCorrection()
        assertEquals(SessionState.REVIEWING, viewModel.state.value)
        assertFalse(viewModel.correctionDiff.value!!.isPerfect)

        // Perfect correction attempt
        viewModel.setCorrectionText("he packed his suitcase")
        viewModel.submitCorrection()
        assertEquals(SessionState.SHADOWING, viewModel.state.value)
        assertTrue(viewModel.correctionDiff.value!!.isPerfect)
    }

    @Test
    fun skipCorrection_transitionsFromReviewingToShadowing() {
        viewModel.setTypedText("he suitcase")
        viewModel.submitAnswer()
        assertEquals(SessionState.REVIEWING, viewModel.state.value)

        viewModel.skipCorrection()
        assertEquals(SessionState.SHADOWING, viewModel.state.value)
    }

    @Test
    fun toggleTranslation_flipsBoolean() {
        assertFalse(viewModel.showTranslation.value)
        viewModel.toggleTranslation()
        assertTrue(viewModel.showTranslation.value)
        viewModel.toggleTranslation()
        assertFalse(viewModel.showTranslation.value)
    }

    @Test
    fun submitEmptyAnswer_staysInDictating() {
        viewModel.setTypedText("")
        viewModel.submitAnswer()

        assertEquals(SessionState.DICTATING, viewModel.state.value)
        assertNull(viewModel.diffResult.value)
    }

    @Test
    fun giveUp_transitionsToReviewingWithZeroAccuracy() {
        viewModel.giveUp()

        assertEquals(SessionState.REVIEWING, viewModel.state.value)
        val diff = viewModel.diffResult.value
        assertNotNull(diff)
        assertEquals(0.0, diff!!.accuracy, 1e-6)
    }

    @Test
    fun nextSegment_advancesOrCompletes() {
        viewModel.setTypedText("he packed his suitcase")
        viewModel.submitAnswer()
        assertEquals(SessionState.SHADOWING, viewModel.state.value)
        viewModel.nextSegment()

        assertEquals(SessionState.DICTATING, viewModel.state.value)
        assertEquals(1, viewModel.currentSegmentIndex.value)

        viewModel.setTypedText("the morning cold hit him")
        viewModel.submitAnswer()
        assertEquals(SessionState.SHADOWING, viewModel.state.value)
        viewModel.nextSegment()

        assertEquals(SessionState.COMPLETED, viewModel.state.value)
    }

    @Test
    fun replaySegment_incrementsCount() {
        assertEquals(0, viewModel.replayCount.value)
        viewModel.replaySegment()
        assertEquals(1, viewModel.replayCount.value)
    }

    @Test
    fun setSpeed_updatesAudioEngineAndState() {
        assertEquals(1.0f, viewModel.speed.value, 1e-6f)
        viewModel.setSpeed(0.75f)
        assertEquals(0.75f, viewModel.speed.value, 1e-6f)
        assertEquals(0.75f, fakeAudioEngine.getSpeed(), 1e-6f)
    }

    @Test
    fun wordMode_submitsWordsSequentially_andAdvancesToShadowing() {
        val fakeSpeech = com.dictalearn.app.domain.audio.FakeSpeechEngine()
        val wordVm = StudySessionViewModel(
            lesson = lesson,
            audioEngine = fakeAudioEngine,
            mistakeRepository = mistakeRepo,
            speechEngine = fakeSpeech,
            initialMode = StudyMode.WORD,
            autoPlay = false
        )

        assertEquals(StudyMode.WORD, wordVm.studyMode.value)
        assertEquals(4, wordVm.targetWords.value.size) // "He packed his suitcase."
        assertEquals(0, wordVm.currentWordIndex.value)
        assertEquals("he", wordVm.currentWord?.clean)

        // Initial speech triggered
        assertTrue(fakeSpeech.spokenWords.contains("he"))

        // Type incorrect word
        wordVm.setTypedWord("she")
        wordVm.submitWord()
        assertEquals(com.dictalearn.app.domain.words.WordFeedback.INCORRECT, wordVm.wordFeedback.value)
        assertEquals(0, wordVm.currentWordIndex.value)

        // Type correct word: "he"
        wordVm.setTypedWord("he")
        wordVm.submitWord()
        assertEquals(com.dictalearn.app.domain.words.WordFeedback.IDLE, wordVm.wordFeedback.value)
        assertEquals(1, wordVm.currentWordIndex.value) // moved to "packed"

        // Use letter hint on "packed"
        wordVm.giveLetterHint()
        assertEquals("p", wordVm.typedWord.value)
        wordVm.giveLetterHint()
        assertEquals("pa", wordVm.typedWord.value)

        // Complete remaining words
        wordVm.setTypedWord("packed")
        wordVm.submitWord()
        assertEquals(2, wordVm.currentWordIndex.value)

        // Skip word 2: "his"
        wordVm.skipWord()
        assertEquals(3, wordVm.currentWordIndex.value) // moved to "suitcase"

        // Submit final word
        wordVm.setTypedWord("suitcase")
        wordVm.submitWord()

        // Advances to SHADOWING upon completing all words
        assertEquals(SessionState.SHADOWING, wordVm.state.value)
    }

    // --- Bug fixes & navigation ---

    @Test
    fun giveUp_isIgnoredOutsideDictating() {
        viewModel.giveUp()
        viewModel.giveUp()
        assertEquals(SessionState.REVIEWING, viewModel.state.value)
        assertEquals(1, viewModel.records.size)
    }

    @Test
    fun wordMode_repeatedWrongAttemptsCountOnce_andAccuracyReflectsMisses() {
        viewModel.setStudyMode(StudyMode.WORD)
        repeat(3) {
            viewModel.setTypedWord("wrong")
            viewModel.submitWord()
        }
        assertEquals(1, mistakeRepo.getMistakes().size)

        listOf("he", "packed", "his", "suitcase").forEach {
            viewModel.setTypedWord(it)
            viewModel.submitWord()
        }
        assertEquals(SessionState.SHADOWING, viewModel.state.value)
        val record = viewModel.records.single()
        assertFalse(record.isPerfect)
        assertEquals(0.75, record.accuracy, 0.001)
    }

    @Test
    fun wordMode_skipAccuracy_isNotHardcoded() {
        viewModel.setStudyMode(StudyMode.WORD)
        repeat(4) { viewModel.skipWord() }
        assertEquals(SessionState.SHADOWING, viewModel.state.value)
        assertEquals(0.0, viewModel.records.single().accuracy, 0.001)
    }

    @Test
    fun initialSegmentIndex_resumesAndIsClamped() {
        val resumed = StudySessionViewModel(lesson, fakeAudioEngine, autoPlay = false, initialSegmentIndex = 1)
        assertEquals(1, resumed.currentSegmentIndex.value)
        assertEquals("The morning cold hit him.", resumed.currentSegment.text)

        val clamped = StudySessionViewModel(lesson, fakeAudioEngine, autoPlay = false, initialSegmentIndex = 42)
        assertEquals(1, clamped.currentSegmentIndex.value)
    }

    @Test
    fun goToSegment_resetsAttempt_fromAnyState() {
        viewModel.setTypedText("he")
        viewModel.submitAnswer()
        assertEquals(SessionState.REVIEWING, viewModel.state.value)

        viewModel.goToSegment(1)
        assertEquals(SessionState.DICTATING, viewModel.state.value)
        assertEquals(1, viewModel.currentSegmentIndex.value)
        assertEquals("", viewModel.typedText.value)
        assertNull(viewModel.diffResult.value)
        assertEquals(3500, fakeAudioEngine.lastStartMs)
    }

    @Test
    fun previousAndSkip_navigateWithinBounds() {
        viewModel.skipSegment()
        assertEquals(1, viewModel.currentSegmentIndex.value)
        viewModel.skipSegment()
        assertEquals(1, viewModel.currentSegmentIndex.value)
        assertEquals(SessionState.DICTATING, viewModel.state.value)
        viewModel.previousSegment()
        assertEquals(0, viewModel.currentSegmentIndex.value)
    }

    @Test
    fun progressAndCompletionCallbacks_fire() {
        val progress = mutableListOf<Int>()
        var completed = 0
        val vm = StudySessionViewModel(
            lesson, fakeAudioEngine, autoPlay = false,
            onProgress = { progress.add(it) },
            onComplete = { completed++ }
        )
        vm.giveUp(); vm.skipCorrection(); vm.nextSegment()
        vm.giveUp(); vm.skipCorrection(); vm.nextSegment()
        assertEquals(listOf(0, 1), progress)
        assertEquals(SessionState.COMPLETED, vm.state.value)
        assertEquals(1, completed)
    }

    @Test
    fun restart_returnsToFirstSegmentWithCleanRecords() {
        viewModel.giveUp(); viewModel.skipCorrection(); viewModel.nextSegment()
        viewModel.restart()
        assertEquals(0, viewModel.currentSegmentIndex.value)
        assertEquals(SessionState.DICTATING, viewModel.state.value)
        assertTrue(viewModel.records.isEmpty())
    }

    @Test
    fun extendLesson_appendsSegments_withoutResettingTheSession() {
        viewModel.giveUp(); viewModel.skipCorrection(); viewModel.nextSegment()
        assertEquals(1, viewModel.currentSegmentIndex.value)

        val longer = lesson.copy(segments = lesson.segments + Segment(id = 3, startMs = 7000, endMs = 9000, text = "A third sentence."))
        viewModel.extendLesson(longer)
        assertEquals(3, viewModel.totalSegmentsFlow.value)
        assertEquals(1, viewModel.currentSegmentIndex.value)
        assertEquals(SessionState.DICTATING, viewModel.state.value)

        // shorter or different lessons are ignored
        viewModel.extendLesson(lesson)
        assertEquals(3, viewModel.totalSegmentsFlow.value)
    }

    @Test
    fun onRecord_reportsFirstAttemptsOnly() {
        val recorded = mutableListOf<SegmentRecord>()
        val vm = StudySessionViewModel(lesson, fakeAudioEngine, autoPlay = false, onRecord = { recorded.add(it) })
        vm.setTypedText("he")
        vm.submitAnswer()
        vm.setCorrectionText("He packed his suitcase.")
        vm.submitCorrection()
        assertEquals(1, recorded.size)
        assertTrue(recorded.single().accuracy < 0.7)
    }
}
