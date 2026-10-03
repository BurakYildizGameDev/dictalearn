package com.dictalearn.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import com.dictalearn.app.data.audio.MediaPlayerAudioEngine
import com.dictalearn.app.data.mistakes.InMemoryMistakeRepository
import com.dictalearn.app.domain.parser.LessonParser
import com.dictalearn.app.ui.StudySessionScreen
import com.dictalearn.app.ui.StudySessionViewModel

class MainActivity : ComponentActivity() {

    companion object {
        init {
            System.loadLibrary("dictalearn_native")
        }
    }

    external fun stringFromJNI(): String

    private lateinit var audioEngine: MediaPlayerAudioEngine

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        audioEngine = MediaPlayerAudioEngine(this)

        setContent {
            var viewModel by remember { mutableStateOf<StudySessionViewModel?>(null) }
            var error by remember { mutableStateOf<String?>(null) }

            LaunchedEffect(Unit) {
                try {
                    val json = assets.open("lessons/sample_ch01/lesson.json").bufferedReader().use { it.readText() }
                    val result = LessonParser.parse(json)
                    if (result.isValid && result.lesson != null) {
                        audioEngine.load("assets/lessons/sample_ch01/audio.wav")
                        val mistakeRepo = InMemoryMistakeRepository()
                        viewModel = StudySessionViewModel(
                            lesson = result.lesson,
                            audioEngine = audioEngine,
                            mistakeRepository = mistakeRepo,
                            autoPlay = true
                        )
                    } else {
                        error = result.errors.joinToString("\n")
                    }
                } catch (e: Exception) {
                    error = e.message ?: "Ders yüklenirken hata oluştu."
                }
            }

            Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                val vm = viewModel
                if (vm != null) {
                    StudySessionScreen(viewModel = vm)
                } else if (error != null) {
                    Text(text = "Hata: $error")
                } else {
                    CircularProgressIndicator()
                }
            }
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        audioEngine.dispose()
    }
}
