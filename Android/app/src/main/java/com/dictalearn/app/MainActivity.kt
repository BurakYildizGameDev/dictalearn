package com.dictalearn.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.SystemBarStyle
import androidx.activity.enableEdgeToEdge
import androidx.activity.compose.BackHandler
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material3.Button
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.dictalearn.app.data.audio.AndroidSpeechEngine
import com.dictalearn.app.data.audio.MediaPlayerAudioEngine
import com.dictalearn.app.data.mistakes.PersistentMistakeRepository
import com.dictalearn.app.data.storage.SharedPrefsKeyValueStore
import com.dictalearn.app.domain.library.CatalogBook
import com.dictalearn.app.domain.library.LessonCatalog
import com.dictalearn.app.domain.model.Lesson
import com.dictalearn.app.domain.parser.LessonParser
import com.dictalearn.app.domain.progress.ProgressStore
import com.dictalearn.app.ui.LessonEditorScreen
import com.dictalearn.app.ui.LibraryScreen
import com.dictalearn.app.ui.StudyMode
import com.dictalearn.app.ui.StudySessionScreen
import com.dictalearn.app.ui.StudySessionViewModel
import com.dictalearn.app.ui.theme.Dicta
import com.dictalearn.app.ui.theme.DictaTheme
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

private sealed interface Screen {
    data object Library : Screen
    data class Study(val book: CatalogBook) : Screen
    data object Editor : Screen
    data object CustomStudy : Screen
}

private const val KEY_LAST_BOOK = "last_book"
private const val KEY_SPEED = "audio_speed"
private const val KEY_AUTOPLAY = "autoplay"
private const val KEY_MODE = "study_mode"

class MainActivity : ComponentActivity() {

    companion object {
        init {
            System.loadLibrary("dictalearn_native")
        }
    }

    external fun stringFromJNI(): String

    private lateinit var audioEngine: MediaPlayerAudioEngine
    private lateinit var speechEngine: AndroidSpeechEngine

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // The app is always dark; edge-to-edge also makes IME insets available to Compose.
        enableEdgeToEdge(
            statusBarStyle = SystemBarStyle.dark(android.graphics.Color.TRANSPARENT),
            navigationBarStyle = SystemBarStyle.dark(android.graphics.Color.TRANSPARENT)
        )
        audioEngine = MediaPlayerAudioEngine(this)
        speechEngine = AndroidSpeechEngine(this)

        val prefs = SharedPrefsKeyValueStore(this)
        val progressStore = ProgressStore(prefs)
        val mistakeRepo = PersistentMistakeRepository(prefs)
        val availableBooks = LessonCatalog.onlyAvailable(assets.list("lessons")?.toSet().orEmpty())

        setContent {
            DictaTheme {
                var screen by remember { mutableStateOf<Screen>(Screen.Library) }
                var progress by remember { mutableStateOf(progressStore.all()) }
                var lastBookId by remember { mutableStateOf(prefs.getString(KEY_LAST_BOOK)) }
                var viewModel by remember { mutableStateOf<StudySessionViewModel?>(null) }
                var loadedLesson by remember { mutableStateOf<Lesson?>(null) }
                var error by remember { mutableStateOf<String?>(null) }
                var retryKey by remember { mutableIntStateOf(0) }
                val audioStatus by audioEngine.status.collectAsState()

                fun newViewModel(lesson: Lesson, lessonKey: String?, startIndex: Int): StudySessionViewModel =
                    StudySessionViewModel(
                        lesson = lesson,
                        audioEngine = audioEngine,
                        mistakeRepository = mistakeRepo,
                        autoPlay = prefs.getString(KEY_AUTOPLAY) == "true",
                        speechEngine = speechEngine,
                        initialMode = if (prefs.getString(KEY_MODE) == "WORD") StudyMode.WORD else StudyMode.SENTENCE,
                        initialSegmentIndex = startIndex,
                        initialSpeed = prefs.getString(KEY_SPEED)?.toFloatOrNull() ?: 1.0f,
                        onProgress = { index ->
                            if (lessonKey != null) {
                                progressStore.record(lessonKey, index, lesson.segments.size)
                                progress = progressStore.all()
                            }
                        },
                        onComplete = {
                            if (lessonKey != null) {
                                progressStore.markCompleted(lessonKey, lesson.segments.size)
                                progress = progressStore.all()
                            }
                        }
                    )

                fun goToLibrary() {
                    audioEngine.pause()
                    speechEngine.stop()
                    screen = Screen.Library
                }

                BackHandler(enabled = screen != Screen.Library) { goToLibrary() }

                // Load lesson JSON off the main thread; audio prepares asynchronously.
                val studyBook = (screen as? Screen.Study)?.book
                LaunchedEffect(studyBook, retryKey) {
                    val book = studyBook ?: return@LaunchedEffect
                    viewModel = null
                    error = null
                    try {
                        val result = withContext(Dispatchers.IO) {
                            val json = assets.open(book.lessonAssetPath).bufferedReader().use { it.readText() }
                            LessonParser.parse(json)
                        }
                        val lesson = result.lesson
                        if (!result.isValid || lesson == null) {
                            error = result.errors.joinToString("\n")
                            return@LaunchedEffect
                        }
                        audioEngine.load("assets/${book.audioAssetPath}")
                        val saved = progressStore.get(book.id)
                        val start = if (saved != null && !saved.completed) saved.segmentIndex else 0
                        loadedLesson = lesson
                        viewModel = newViewModel(lesson, book.id, start)
                        lastBookId = book.id
                        prefs.putString(KEY_LAST_BOOK, book.id)
                    } catch (e: Exception) {
                        error = e.message ?: "Ders yüklenirken hata oluştu."
                    }
                }

                // Persist user preferences whenever the session changes them.
                viewModel?.let { vm ->
                    val speed by vm.speed.collectAsState()
                    val autoPlay by vm.autoPlay.collectAsState()
                    val mode by vm.studyMode.collectAsState()
                    LaunchedEffect(speed, autoPlay, mode) {
                        prefs.putString(KEY_SPEED, speed.toString())
                        prefs.putString(KEY_AUTOPLAY, autoPlay.toString())
                        prefs.putString(KEY_MODE, mode.name)
                    }
                }

                Box(
                    modifier = Modifier
                        .fillMaxSize()
                        .background(Dicta.Background)
                ) {
                    when (val s = screen) {
                        Screen.Library -> LibraryScreen(
                            books = availableBooks,
                            progress = progress,
                            lastBookId = lastBookId,
                            onOpenBook = { screen = Screen.Study(it) },
                            onOpenEditor = { screen = Screen.Editor }
                        )

                        Screen.Editor -> Box(Modifier.systemBarsPadding()) { LessonEditorScreen(
                            initialLesson = loadedLesson,
                            onStartLesson = { newLesson ->
                                loadedLesson = newLesson
                                viewModel = newViewModel(newLesson, null, 0)
                                screen = Screen.CustomStudy
                            },
                            onCancel = { goToLibrary() }
                        ) }

                        is Screen.Study, Screen.CustomStudy -> {
                            val vm = viewModel
                            when {
                                error != null -> Box(Modifier.systemBarsPadding()) { ErrorState(
                                    message = error!!,
                                    onRetry = { retryKey++ },
                                    onBack = { goToLibrary() }
                                ) }
                                vm == null -> Box(Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                                    CircularProgressIndicator(color = Dicta.Accent)
                                }
                                else -> StudySessionScreen(
                                    viewModel = vm,
                                    title = (s as? Screen.Study)?.book?.title ?: vm.lesson.title,
                                    audioStatus = audioStatus,
                                    onPause = { audioEngine.pause() },
                                    onBack = { goToLibrary() }
                                )
                            }
                        }
                    }
                }
            }
        }
    }

    override fun onStop() {
        super.onStop()
        // Don't keep talking when the app goes to the background.
        audioEngine.pause()
        speechEngine.stop()
    }

    override fun onDestroy() {
        super.onDestroy()
        audioEngine.dispose()
        speechEngine.dispose()
    }
}

@Composable
private fun ErrorState(message: String, onRetry: () -> Unit, onBack: () -> Unit) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(24.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text("Ders yüklenemedi", color = Dicta.Error)
        Spacer(Modifier.height(8.dp))
        Text(message, color = Dicta.TextSecondary)
        Spacer(Modifier.height(16.dp))
        Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
            OutlinedButton(onClick = onBack) { Text("Kütüphane") }
            Button(onClick = onRetry) { Text("Yeniden dene") }
        }
    }
}
