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
}
