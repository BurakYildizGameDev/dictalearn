package com.dictalearn.app.domain.library

import java.text.Normalizer

/** One entry of the bundled library (assets/lessons/<id>/). Mirrors Web/src/domain/library/catalog.ts. */
data class CatalogBook(
    val id: String,
    val title: String,
    val titleTr: String?,
    val author: String,
    /** 0 = demo, 1 = A2 (15 pages), 2 = B1 (25 pages), 3 = B2, 4 = C1 */
    val level: Int,
    val pages: Int,
    val sentences: Int
) {
    val lessonAssetPath: String get() = "lessons/$id/lesson.json"

    // MP3 only: the WAV masters are excluded from the APK (see app/build.gradle.kts).
    val audioAssetPath: String get() = "lessons/$id/audio.mp3"
}

object LessonCatalog {

    val levelLabels: Map<Int, String> = mapOf(
        0 to "Demo",
        1 to "A2 · 15 sayfa",
        2 to "B1 · 25 sayfa",
        3 to "B2 · 35 sayfa",
        4 to "C1 · 50 sayfa"
    )

    val levelShort: Map<Int, String> = mapOf(0 to "Demo", 1 to "A2", 2 to "B1", 3 to "B2", 4 to "C1")

    private fun l1(id: String, title: String, author: String, tr: String) =
        CatalogBook(id, title, tr, author, level = 1, pages = 15, sentences = 300)

    private fun l2(id: String, title: String, author: String, tr: String) =
        CatalogBook(id, title, tr, author, level = 2, pages = 25, sentences = 500)

    val books: List<CatalogBook> = listOf(
        l1("book_01_the_happy_prince", "The Happy Prince", "Oscar Wilde", "Mutlu Prens"),
        l1("book_02_the_selfish_giant", "The Selfish Giant", "Oscar Wilde", "Bencil Dev"),
        l1("book_03_the_nightingale_and_the_rose", "The Nightingale and the Rose", "Oscar Wilde", "Bülbül ile Gül"),
        l1("book_04_the_devoted_friend", "The Devoted Friend", "Oscar Wilde", "Sadık Dost"),
        l1("book_05_the_remarkable_rocket", "The Remarkable Rocket", "Oscar Wilde", "Olağanüstü Roket"),
        l1("book_06_aesops_fables_part1", "Aesop's Fables · Part 1", "Aesop", "Ezop Masalları 1"),
        l1("book_07_aesops_fables_part2", "Aesop's Fables · Part 2", "Aesop", "Ezop Masalları 2"),
        l1("book_08_the_little_prince", "The Little Prince", "Antoine de Saint-Exupéry", "Küçük Prens"),
        l1("book_09_grimms_fairy_tales", "Grimm's Fairy Tales", "Brothers Grimm", "Grimm Masalları"),
        l1("book_10_hans_christian_andersen", "Tales of Wonder", "Hans Christian Andersen", "Andersen Masalları"),
        l1("book_11_alices_adventures_in_wonderland", "Alice's Adventures in Wonderland", "Lewis Carroll", "Alice Harikalar Diyarında"),
        l1("book_12_the_adventures_of_pinocchio", "The Adventures of Pinocchio", "Carlo Collodi", "Pinokyo'nun Maceraları"),
        l1("book_13_the_wonderful_wizard_of_oz", "The Wonderful Wizard of Oz", "L. Frank Baum", "Oz Büyücüsü"),
        l1("book_14_the_jungle_book", "The Jungle Book", "Rudyard Kipling", "Orman Çocuğu"),
        l1("book_15_the_wind_in_the_willows", "The Wind in the Willows", "Kenneth Grahame", "Söğütlerdeki Rüzgâr"),
        l1("book_16_peter_pan", "Peter Pan", "J. M. Barrie", "Peter Pan"),
        l1("book_17_the_merry_adventures_of_robin_hood", "The Merry Adventures of Robin Hood", "Howard Pyle", "Robin Hood'un Maceraları"),
        l1("book_18_king_arthur", "King Arthur and the Knights", "Howard Pyle", "Kral Arthur"),
        l1("book_19_gullivers_travels", "Gulliver's Travels", "Jonathan Swift", "Gulliver'in Gezileri"),
        l1("book_20_treasure_island", "Treasure Island", "Robert Louis Stevenson", "Define Adası"),
        l1("book_21_around_the_world_in_eighty_days", "Around the World in Eighty Days", "Jules Verne", "80 Günde Devr-i Âlem"),
        l1("book_22_a_christmas_carol", "A Christmas Carol", "Charles Dickens", "Bir Noel Şarkısı"),
        l1("book_23_the_secret_garden", "The Secret Garden", "Frances Hodgson Burnett", "Gizli Bahçe"),
        l1("book_24_white_fang", "White Fang", "Jack London", "Beyaz Diş"),
        l1("book_25_the_time_machine", "The Time Machine", "H. G. Wells", "Zaman Makinesi"),
        l2("book_26_a_scandal_in_bohemia", "A Scandal in Bohemia", "Arthur Conan Doyle", "Bohemya'da Skandal"),
        l2("book_27_the_red_headed_league", "The Red-Headed League", "Arthur Conan Doyle", "Kızıl Saçlılar Kulübü"),
        l2("book_28_the_hound_of_the_baskervilles", "The Hound of the Baskervilles", "Arthur Conan Doyle", "Baskerville'lerin Köpeği"),
        l2("book_29_the_gift_of_the_magi", "The Gift of the Magi & The Last Leaf", "O. Henry", "Müneccimlerin Hediyesi & Son Yaprak"),
        l2("book_30_the_call_of_the_wild", "The Call of the Wild", "Jack London", "Vahşetin Çağrısı"),
        l2("book_31_frankenstein", "Frankenstein", "Mary Shelley", "Frankenstein"),
        l2("book_32_dracula", "Dracula", "Bram Stoker", "Drakula"),
        l2("book_33_dr_jekyll_and_mr_hyde", "Dr. Jekyll and Mr. Hyde", "Robert Louis Stevenson", "Dr. Jekyll ve Bay Hyde"),
        l2("book_34_the_picture_of_dorian_gray", "The Picture of Dorian Gray", "Oscar Wilde", "Dorian Gray'in Portresi"),
        l2("book_35_the_canterville_ghost", "The Canterville Ghost", "Oscar Wilde", "Canterville Hayaleti"),
        l2("book_36_journey_to_the_center_of_the_earth", "Journey to the Center of the Earth", "Jules Verne", "Dünyanın Merkezine Yolculuk"),
        CatalogBook("sample_ch01", "The Departure", "Demo ders", "DictaLearn", level = 0, pages = 1, sentences = 6)
    )

    fun find(id: String): CatalogBook? = books.firstOrNull { it.id == id }

    /** Keeps catalog order but only books whose asset folder exists. */
    fun onlyAvailable(assetDirs: Set<String>): List<CatalogBook> = books.filter { it.id in assetDirs }

    private val marks = Regex("\\p{M}+")

    // Locale-neutral folding so "DRACULA", "Çağrısı" and "cagrisi" match.
    private fun fold(s: String): String =
        Normalizer.normalize(s.lowercase(), Normalizer.Form.NFD).replace(marks, "").replace('ı', 'i')

    fun filter(books: List<CatalogBook>, level: Int?, query: String): List<CatalogBook> {
        val q = fold(query.trim())
        return books.filter { b ->
            (level == null || b.level == level) &&
                (q.isEmpty() || listOf(b.title, b.titleTr.orEmpty(), b.author).any { fold(it).contains(q) })
        }
    }
}
