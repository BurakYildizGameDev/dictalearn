package com.dictalearn.app.domain

import com.dictalearn.app.domain.audio.AudioStatus
import com.dictalearn.app.domain.audio.FakeAudioEngine
import org.junit.Assert.*
import org.junit.Test

class AudioEngineTest {

    @Test
    fun fakeAudioEngine_playRange_updatesStatusAndCounts() {
        val engine = FakeAudioEngine()
        assertEquals(AudioStatus.IDLE, engine.status.value)

        engine.playRange(1000, 3000)
        assertEquals(AudioStatus.PLAYING, engine.status.value)
        assertEquals(1, engine.playCount)
        assertEquals(1000, engine.lastStartMs)
        assertEquals(3000, engine.lastEndMs)

        engine.completeRange()
        assertEquals(AudioStatus.RANGE_COMPLETED, engine.status.value)
    }

    @Test
    fun fakeAudioEngine_speedControl() {
        val engine = FakeAudioEngine()
        assertEquals(1.0f, engine.getSpeed())

        engine.setSpeed(1.25f)
        assertEquals(1.25f, engine.getSpeed())
    }
}
