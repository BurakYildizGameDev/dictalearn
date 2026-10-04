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
import com.dictalearn.app.data.audio.WordAudioSpeechEngine
import com.dictalearn.app.data.audio.TtsSegmentAudioEngine
import com.dictalearn.app.data.pdf.PdfPagesJobs
import com.dictalearn.app.data.pdf.PdfPagesState
import com.dictalearn.app.data.pdf.UserPdf
import com.dictalearn.app.data.pdf.UserPdfStore
import com.dictalearn.app.domain.audio.AudioEngine
import com.dictalearn.app.domain.pdflesson.PdfLesson
import com.dictalearn.app.domain.review.SrsStore
import com.dictalearn.app.domain.review.HardSentenceStore
import com.dictalearn.app.domain.progress.DailyStats
import com.dictalearn.app.ui.DailySnapshot
import com.dictalearn.app.ui.ReviewScreen
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import kotlinx.coroutines.launch
import com.dictalearn.app.data.mistakes.PersistentMistakeRepository
import com.dictalearn.app.data.storage.SharedPrefsKeyValueStore
import com.dictalearn.app.domain.library.CatalogBook
import com.dictalearn.app.domain.library.LessonCatalog
import com.dictalearn.app.data.translation.MlKitTranslator
import com.dictalearn.app.domain.dictionary.Dictionary
import com.dictalearn.app.domain.mistakes.MistakeKind
import com.dictalearn.app.domain.mistakes.MistakeRecord
import com.dictalearn.app.domain.model.Lesson
import com.dictalearn.app.domain.parser.LessonParser
import com.dictalearn.app.domain.progress.ProgressStore
import com.dictalearn.app.ui.LessonEditorScreen
import com.dictalearn.app.ui.LibraryScreen
import com.dictalearn.app.ui.LocalWordTools
import com.dictalearn.app.ui.NotebookScreen
import com.dictalearn.app.ui.PdfReaderScreen
import com.dictalearn.app.ui.WordTools
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
    data object Notebook : Screen
    data class PdfLesson(val pdf: UserPdf) : Screen
    data class PdfRead(val pdf: UserPdf) : Screen
    data object Review : Screen
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
    private lateinit var speechEngine: WordAudioSpeechEngine
    private lateinit var ttsEngine: TtsSegmentAudioEngine
    private val translator by lazy { MlKitTranslator() }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // The app is always dark; edge-to-edge also makes IME insets available to Compose.
        enableEdgeToEdge(
            statusBarStyle = SystemBarStyle.dark(android.graphics.Color.TRANSPARENT),
            navigationBarStyle = SystemBarStyle.dark(android.graphics.Color.TRANSPARENT)
        )
        audioEngine = MediaPlayerAudioEngine(this)
        speechEngine = WordAudioSpeechEngine(this, fallback = AndroidSpeechEngine(this))
        ttsEngine = TtsSegmentAudioEngine(this)

        val prefs = SharedPrefsKeyValueStore(this)
        val progressStore = ProgressStore(prefs)
        val mistakeRepo = PersistentMistakeRepository(prefs)
        val availableBooks = LessonCatalog.onlyAvailable(assets.list("lessons")?.toSet().orEmpty())
        val pdfStore = UserPdfStore(this, prefs)
        val pagesJobs = PdfPagesJobs(this)
        val srs = SrsStore(prefs)
        val hardStore = HardSentenceStore(prefs)
        val daily = DailyStats(prefs)

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
                var showPdf by remember { mutableStateOf(false) }
                var dictionary by remember { mutableStateOf<Dictionary?>(null) }
                var userPdfs by remember { mutableStateOf(pdfStore.list()) }
                var pagesState by remember { mutableStateOf<PdfPagesState?>(null) }
                var hardVersion by remember { mutableIntStateOf(0) }
                var dailyVersion by remember { mutableIntStateOf(0) }
                // Short round over the hard sentences of the current lesson (null = normal study).
                var hardVm by remember { mutableStateOf<StudySessionViewModel?>(null) }
                val ttsStatus by ttsEngine.status.collectAsState()
                val scope = rememberCoroutineScope()

                val pickPdf = rememberLauncherForActivityResult(ActivityResultContracts.OpenDocument()) { uri ->
                    if (uri != null) {
                        scope.launch {
                            runCatching { withContext(Dispatchers.IO) { pdfStore.add(uri) } }
                            userPdfs = pdfStore.list()
                        }
                    }
                }

                LaunchedEffect(Unit) {
                    dictionary = withContext(Dispatchers.IO) {
                        runCatching {
                            Dictionary.fromJson(assets.open("lessons/dictionary.json").bufferedReader().use { it.readText() })
                        }.getOrNull()
                    }
                }

                val wordTools = remember(dictionary) {
                    WordTools(
                        dictionary = dictionary,
                        translator = translator,
                        speak = { speechEngine.speak(it) },
                        addUnknown = { word, lessonId, segmentId ->
                            mistakeRepo.addMistakes(listOf(MistakeRecord(word, MistakeKind.UNKNOWN, null, lessonId, segmentId)))
                        }
                    )
                }

                fun newViewModel(
                    lesson: Lesson,
                    lessonKey: String?,
                    startIndex: Int,
                    engine: AudioEngine = audioEngine,
                    hardKey: String? = lessonKey
                ): StudySessionViewModel =
                    StudySessionViewModel(
                        lesson = lesson,
                        audioEngine = engine,
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
                        },
                        onRecord = { record ->
                            daily.addSentence()
                            dailyVersion++
                            if (hardKey != null) {
                                hardStore.record(hardKey, record.segmentId, record.accuracy)
                                hardVersion++
                            }
                        }
                    )

                fun startHardRound(vm: StudySessionViewModel, key: String, engine: AudioEngine) {
                    val sub = HardSentenceStore.subLesson(vm.lesson, hardStore.list(key))
                    if (sub.segments.isNotEmpty()) hardVm = newViewModel(sub, null, 0, engine, hardKey = key)
                }

                fun goToLibrary() {
                    audioEngine.pause()
                    ttsEngine.pause()
                    speechEngine.stop()
                    showPdf = false
                    hardVm = null
                    screen = Screen.Library
                }

                BackHandler(enabled = screen != Screen.Library) {
                    when {
                        showPdf -> showPdf = false
                        hardVm != null -> hardVm = null
                        screen == Screen.Review -> screen = Screen.Notebook
                        else -> goToLibrary()
                    }
                }

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

                // Lesson from a user PDF: pages are OCR'd in order; the lesson opens after the first 25
                // pages and keeps growing while the rest are read in the background.
                val pdfLesson = (screen as? Screen.PdfLesson)?.pdf
                LaunchedEffect(pdfLesson, retryKey) {
                    val pdf = pdfLesson ?: return@LaunchedEffect
                    viewModel = null
                    error = null
                    pagesState = null
                    audioEngine.pause()
                    val key = "pdf_${pdf.id}"
                    var lastCount = -1
                    pagesJobs.state(pdf.id, pdfStore.file(pdf.id)).collect { state ->
                        pagesState = state
                        if (state.error != null) {
                            error = state.error
                            return@collect
                        }
                        val done = state.contiguousDone
                        val finished = !state.running
                        if (state.totalPages == 0 || (done < PdfLesson.firstBatchSize(state.totalPages) && !finished)) return@collect
                        val sentences = withContext(Dispatchers.Default) {
                            PdfLesson.extractSentences(state.texts.take(done).filterNotNull().joinToString("\n"))
                        }
                        if (sentences.size == lastCount) return@collect
                        lastCount = sentences.size
                        val vm = viewModel
                        if (vm == null) {
                            if (sentences.isEmpty()) {
                                if (finished) error = "Bu PDF'te dikte için İngilizce cümle bulunamadı."
                                return@collect
                            }
                            val lesson = PdfLesson.buildLesson(key, pdf.name, sentences)
                            ttsEngine.setSegments(lesson.segments)
                            val saved = progressStore.get(key)
                            val start = if (saved != null && !saved.completed) saved.segmentIndex.coerceAtMost(sentences.size - 1) else 0
                            viewModel = newViewModel(lesson, key, start, ttsEngine)
                        } else {
                            val merged = PdfLesson.mergeSentences(vm.lesson.segments.map { it.text }, sentences)
                            val lesson = PdfLesson.buildLesson(key, pdf.name, merged)
                            ttsEngine.setSegments(lesson.segments)
                            vm.extendLesson(lesson)
                        }
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

                CompositionLocalProvider(LocalWordTools provides wordTools) {
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
                            onOpenEditor = { screen = Screen.Editor },
                            onOpenNotebook = { screen = Screen.Notebook },
                            userPdfs = userPdfs,
                            onAddPdf = { pickPdf.launch(arrayOf("application/pdf")) },
                            onStudyPdf = { screen = Screen.PdfLesson(it) },
                            onReadPdf = { screen = Screen.PdfRead(it) },
                            daily = dailyVersion.let {
                                DailySnapshot(daily.todayCount(), daily.goal(), daily.streak(), daily.lastDays(7))
                            },
                            onGoalChange = {
                                daily.setGoal(it)
                                dailyVersion++
                            },
                            onDeletePdf = { pdf ->
                                pagesJobs.cancel(pdf.id)
                                pdfStore.remove(pdf.id)
                                userPdfs = pdfStore.list()
                            }
                        )

                        is Screen.PdfRead -> PdfReaderScreen(
                            assetPath = null,
                            localFile = pdfStore.file(s.pdf.id),
                            title = s.pdf.name,
                            onBack = { goToLibrary() }
                        )

                        is Screen.PdfLesson -> {
                            val vm = viewModel
                            val pages = pagesState
                            when {
                                error != null -> Box(Modifier.systemBarsPadding()) { ErrorState(
                                    message = error!!,
                                    onRetry = { retryKey++ },
                                    onBack = { goToLibrary() }
                                ) }
                                vm == null -> PdfLoadingState(pages)
                                showPdf -> PdfReaderScreen(
                                    assetPath = null,
                                    localFile = pdfStore.file(s.pdf.id),
                                    title = s.pdf.name,
                                    onBack = { showPdf = false }
                                )
                                hardVm != null -> StudySessionScreen(
                                    viewModel = hardVm!!,
                                    title = s.pdf.name,
                                    audioStatus = ttsStatus,
                                    onPause = { ttsEngine.pause() },
                                    onBack = { hardVm = null },
                                    hardMode = true
                                )
                                else -> StudySessionScreen(
                                    viewModel = vm,
                                    title = vm.lesson.title,
                                    audioStatus = ttsStatus,
                                    onPause = { ttsEngine.pause() },
                                    onBack = { goToLibrary() },
                                    onOpenPdf = {
                                        ttsEngine.pause()
                                        showPdf = true
                                    },
                                    banner = { PdfLessonBanner(pages) },
                                    hardCount = hardVersion.let { hardStore.count("pdf_${s.pdf.id}") },
                                    onReviewHard = { startHardRound(vm, "pdf_${s.pdf.id}", ttsEngine) }
                                )
                            }
                        }

                        Screen.Notebook -> NotebookScreen(
                            repository = mistakeRepo,
                            dictionary = dictionary,
                            onSpeak = { speechEngine.speak(it) },
                            onBack = { goToLibrary() },
                            srs = srs,
                            onStartReview = { screen = Screen.Review }
                        )

                        Screen.Review -> ReviewScreen(
                            srs = srs,
                            dictionary = dictionary,
                            onSpeak = { speechEngine.speak(it) },
                            onBack = { screen = Screen.Notebook }
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
                                showPdf && (s as? Screen.Study)?.book?.pdfAssetPath != null -> PdfReaderScreen(
                                    assetPath = s.book.pdfAssetPath!!,
                                    title = s.book.title,
                                    onBack = { showPdf = false }
                                )
                                hardVm != null -> StudySessionScreen(
                                    viewModel = hardVm!!,
                                    title = (s as? Screen.Study)?.book?.title ?: vm.lesson.title,
                                    audioStatus = audioStatus,
                                    onPause = { audioEngine.pause() },
                                    onBack = { hardVm = null },
                                    hardMode = true
                                )
                                else -> StudySessionScreen(
                                    viewModel = vm,
                                    hardCount = (s as? Screen.Study)?.book?.id?.let { id -> hardVersion.let { hardStore.count(id) } } ?: 0,
                                    onReviewHard = (s as? Screen.Study)?.book?.id?.let { id -> { startHardRound(vm, id, audioEngine) } },
                                    title = (s as? Screen.Study)?.book?.title ?: vm.lesson.title,
                                    audioStatus = audioStatus,
                                    onPause = { audioEngine.pause() },
                                    onBack = { goToLibrary() },
                                    onOpenPdf = (s as? Screen.Study)?.book?.pdfAssetPath?.let {
                                        {
                                            audioEngine.pause()
                                            showPdf = true
                                        }
                                    }
                                )
                            }
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
        ttsEngine.pause()
        speechEngine.stop()
    }

    override fun onDestroy() {
        super.onDestroy()
        audioEngine.dispose()
        ttsEngine.dispose()
        speechEngine.dispose()
        translator.close()
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

@Composable
private fun PdfLoadingState(pages: PdfPagesState?) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .systemBarsPadding()
            .padding(32.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        CircularProgressIndicator(color = Dicta.Accent)
        Spacer(Modifier.height(16.dp))
        val total = pages?.totalPages ?: 0
        Text(
            if (total == 0) "PDF açılıyor…"
            else "Sayfalar okunuyor: ${pages!!.contiguousDone} / ${PdfLesson.firstBatchSize(total)}",
            color = Dicta.TextPrimary
        )
        Spacer(Modifier.height(8.dp))
        Text(
            "Sayfalar metin tanıma (OCR) ile okunuyor. İlk ${PdfLesson.FIRST_BATCH_PAGES} sayfa bitince ders açılır, kalanı arka planda devam eder.",
            color = Dicta.TextMuted
        )
    }
}

@Composable
private fun PdfLessonBanner(pages: PdfPagesState?) {
    if (pages == null) return
    Column(verticalArrangement = Arrangement.spacedBy(6.dp)) {
        if (pages.running && pages.totalPages > 0) {
            Text(
                "Arka planda okunuyor: ${pages.contiguousDone} / ${pages.totalPages} sayfa · yeni cümleler derse ekleniyor",
                color = Dicta.Accent
            )
        }
        Text(
            "Bu ders PDF'ten metin tanıma (OCR) ile oluşturuldu; nadiren yanlış tanınan kelimeler olabilir.",
            color = Dicta.TextMuted
        )
    }
}
