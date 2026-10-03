package com.dictalearn.app.ui

import com.dictalearn.app.domain.audio.FakeAudioEngine
import com.dictalearn.app.domain.model.Lesson
import com.dictalearn.app.domain.model.Segment
import org.junit.Assert.*
import org.junit.Before
import org.junit.Test

class StudySessionViewModelTest {

    private lateinit var lesson: Lesson
    private lateinit var fakeAudioEngine: FakeAudioEngine
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
        viewModel = StudySessionViewModel(lesson, fakeAudioEngine, autoPlay = true)
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
    fun submitAnswer_transitionsToReviewing() {
        viewModel.setTypedText("he packed his suitcase")
        viewModel.submitAnswer()

        assertEquals(SessionState.REVIEWING, viewModel.state.value)
        val diff = viewModel.diffResult.value
        assertNotNull(diff)
        assertTrue(diff!!.isPerfect)
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
        viewModel.nextSegment()

        assertEquals(SessionState.DICTATING, viewModel.state.value)
        assertEquals(1, viewModel.currentSegmentIndex.value)

        viewModel.setTypedText("the morning cold hit him")
        viewModel.submitAnswer()
        viewModel.nextSegment()

        assertEquals(SessionState.COMPLETED, viewModel.state.value)
    }

    @Test
    fun replaySegment_incrementsCount() {
        assertEquals(0, viewModel.replayCount.value)
        viewModel.replaySegment()
        assertEquals(1, viewModel.replayCount.value)
    }
}
