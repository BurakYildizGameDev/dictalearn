import javax.inject.Inject

plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
}

// `-Pdictalearn.abiSplits=true` (release workflow): one APK per CPU architecture instead of one
// universal APK, so the ML Kit / C++ native libraries are not shipped four times.
val abiSplits = project.findProperty("dictalearn.abiSplits") == "true"

/**
 * Copies src/main/assets into the APK assets without the WAV masters and preview markdown, and with
 * the audio/PDF of only [bundledBooks]; every other book (and the word audio sprites) is downloaded
 * by the app from GitHub Pages on first use (BookStore). lesson.json files and the dictionary are
 * always packaged. `-Pdictalearn.bundleAllBooks=true` builds a fully offline (~600 MB) APK instead.
 */
abstract class PrepareBookAssets @Inject constructor(private val fs: FileSystemOperations) : DefaultTask() {
    @get:Internal abstract val sourceDir: DirectoryProperty
    @get:Input abstract val bundledBooks: SetProperty<String>
    @get:Input abstract val bundleAll: Property<Boolean>
    @get:OutputDirectory abstract val outputDir: DirectoryProperty

    // Only the packaged files are inputs, so the multi-GB WAV masters are never hashed.
    @get:InputFiles @get:PathSensitive(PathSensitivity.RELATIVE)
    val packagedFiles: FileTree
        get() = sourceDir.asFileTree.matching { include { packaged(it) } }

    private fun packaged(file: FileTreeElement): Boolean {
        if (file.isDirectory) return true
        val name = file.name
        if (name.endsWith(".wav") || name.endsWith(".md")) return false
        val folder = file.relativePath.segments.getOrNull(1).orEmpty() // lessons/<folder>/...
        if (folder.startsWith("custom_")) return false
        val large = name.endsWith(".mp3") || name.endsWith(".pdf")
        return !large || bundleAll.get() || folder in bundledBooks.get()
    }

    @TaskAction
    fun run() {
        fs.sync {
            from(packagedFiles)
            into(outputDir)
            includeEmptyDirs = false
        }
    }
}

val prepareBookAssets = tasks.register<PrepareBookAssets>("prepareBookAssets") {
    sourceDir.set(layout.projectDirectory.dir("src/main/assets"))
    bundledBooks.set(setOf("sample_ch01", "book_01_the_happy_prince"))
    bundleAll.set(project.findProperty("dictalearn.bundleAllBooks") == "true")
    outputDir.set(layout.buildDirectory.dir("generated/bookAssets"))
}

android {
    namespace = "com.dictalearn.app"
    compileSdk = 36
    ndkVersion = "28.2.13676358"

    defaultConfig {
        applicationId = "com.dictalearn.app"
        minSdk = 24
        targetSdk = 36
        versionCode = 2
        versionName = "1.1.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
        vectorDrawables {
            useSupportLibrary = true
        }

        externalNativeBuild {
            cmake {
                cppFlags("-std=c++17")
                arguments("-DANDROID_STL=c++_shared")
            }
        }

        if (!abiSplits) {
            ndk {
                abiFilters.addAll(setOf("armeabi-v7a", "arm64-v8a", "x86", "x86_64"))
            }
        }
    }

    // Release signing comes from the environment (CI secrets); without it the APK is unsigned.
    val releaseKeystore = System.getenv("DICTALEARN_KEYSTORE")?.let { file(it) }?.takeIf { it.exists() }
    signingConfigs {
        if (releaseKeystore != null) {
            create("release") {
                storeFile = releaseKeystore
                storePassword = System.getenv("DICTALEARN_KEYSTORE_PASSWORD")
                keyAlias = System.getenv("DICTALEARN_KEY_ALIAS")
                keyPassword = System.getenv("DICTALEARN_KEY_PASSWORD")
            }
        }
    }

    buildTypes {
        release {
            isMinifyEnabled = true
            isShrinkResources = true
            signingConfig = signingConfigs.findByName("release")
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }

    externalNativeBuild {
        cmake {
            path = file("src/main/cpp/CMakeLists.txt")
            version = "3.22.1"
        }
    }

    compileOptions {
        // java.time (spaced repetition dates) on API 24-25
        isCoreLibraryDesugaringEnabled = true
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    kotlinOptions {
        jvmTarget = "17"
    }

    buildFeatures {
        compose = true
        prefab = true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.11"
    }

    if (abiSplits) {
        splits {
            abi {
                isEnable = true
                reset()
                include("arm64-v8a", "armeabi-v7a", "x86_64")
                isUniversalApk = false
            }
        }
    }

    sourceSets["main"].assets.setSrcDirs(emptyList<String>()) // packaged through prepareBookAssets below

    packaging {
        resources {
            excludes += "/META-INF/{AL2.0,LGPL2.1}"
        }
    }
}

androidComponents {
    onVariants { variant ->
        variant.sources.assets?.addGeneratedSourceDirectory(prepareBookAssets, PrepareBookAssets::outputDir)
    }
}

dependencies {
    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.lifecycle.runtime.ktx)
    implementation(libs.androidx.activity.compose)

    implementation(platform(libs.androidx.compose.bom))
    implementation(libs.androidx.ui)
    implementation(libs.androidx.ui.graphics)
    implementation(libs.androidx.ui.tooling.preview)
    implementation(libs.androidx.material3)
    implementation(libs.androidx.material.icons.extended)

    implementation(libs.oboe)
    coreLibraryDesugaring("com.android.tools:desugar_jdk_libs:2.0.4")

    // On-device EN->TR translation (Faz 7.1); the ~30 MB language model downloads on first use.
    implementation("com.google.mlkit:translate:17.0.3")
    // On-device OCR for PDFs (bundled Latin model, works offline)
    implementation("com.google.mlkit:text-recognition:16.0.1")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-play-services:1.7.3")

    testImplementation(libs.junit)
    testImplementation("org.json:json:20240303")
    androidTestImplementation(libs.androidx.junit)
    androidTestImplementation(libs.androidx.espresso.core)
    androidTestImplementation(platform(libs.androidx.compose.bom))
    androidTestImplementation(libs.androidx.ui.testjunit4)
    debugImplementation(libs.androidx.ui.tooling)
    debugImplementation(libs.androidx.ui.testmanifest)
}
