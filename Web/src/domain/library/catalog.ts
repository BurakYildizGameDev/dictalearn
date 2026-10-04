// Static catalog of the bundled lesson library (lessons/<id>/lesson.json + audio.mp3 + optional PDF).

export type BookLevel = 0 | 1 | 2 | 3 | 4
export type BookKind = 'book' | 'demo' | 'personal'

export interface CatalogBook {
  id: string
  title: string
  titleTr?: string
  author: string
  level: BookLevel
  pages: number
  sentences: number
  hasPdf: boolean
  kind: BookKind
  /** Override for PDF files that are not named `<id>.pdf`. */
  pdfFile?: string
}

export const LEVEL_LABELS: Record<BookLevel, { short: string; long: string }> = {
  0: { short: 'Demo', long: 'Demo & Kişisel' },
  1: { short: 'A2', long: 'Seviye 1 · A2 · 15 sayfa' },
  2: { short: 'B1', long: 'Seviye 2 · B1 · 25 sayfa' },
  3: { short: 'B2', long: 'Seviye 3 · B2 · 35 sayfa' },
  4: { short: 'C1', long: 'Seviye 4 · C1 · 50 sayfa' },
}

function level1(id: string, title: string, author: string, titleTr?: string): CatalogBook {
  return { id, title, titleTr, author, level: 1, pages: 15, sentences: 300, hasPdf: true, kind: 'book' }
}

function level2(id: string, title: string, author: string, titleTr?: string): CatalogBook {
  return { id, title, titleTr, author, level: 2, pages: 25, sentences: 500, hasPdf: true, kind: 'book' }
}

export const CATALOG: CatalogBook[] = [
  level1('book_01_the_happy_prince', 'The Happy Prince', 'Oscar Wilde', 'Mutlu Prens'),
  level1('book_02_the_selfish_giant', 'The Selfish Giant', 'Oscar Wilde', 'Bencil Dev'),
  level1('book_03_the_nightingale_and_the_rose', 'The Nightingale and the Rose', 'Oscar Wilde', 'Bülbül ile Gül'),
  level1('book_04_the_devoted_friend', 'The Devoted Friend', 'Oscar Wilde', 'Sadık Dost'),
  level1('book_05_the_remarkable_rocket', 'The Remarkable Rocket', 'Oscar Wilde', 'Olağanüstü Roket'),
  level1('book_06_aesops_fables_part1', "Aesop's Fables · Part 1", 'Aesop', 'Ezop Masalları 1'),
  level1('book_07_aesops_fables_part2', "Aesop's Fables · Part 2", 'Aesop', 'Ezop Masalları 2'),
  level1('book_08_the_little_prince', 'The Little Prince', 'Antoine de Saint-Exupéry', 'Küçük Prens'),
  level1('book_09_grimms_fairy_tales', "Grimm's Fairy Tales", 'Brothers Grimm', 'Grimm Masalları'),
  level1('book_10_hans_christian_andersen', 'Tales of Wonder', 'Hans Christian Andersen', 'Andersen Masalları'),
  level1('book_11_alices_adventures_in_wonderland', "Alice's Adventures in Wonderland", 'Lewis Carroll', 'Alice Harikalar Diyarında'),
  level1('book_12_the_adventures_of_pinocchio', 'The Adventures of Pinocchio', 'Carlo Collodi', "Pinokyo'nun Maceraları"),
  level1('book_13_the_wonderful_wizard_of_oz', 'The Wonderful Wizard of Oz', 'L. Frank Baum', 'Oz Büyücüsü'),
  level1('book_14_the_jungle_book', 'The Jungle Book', 'Rudyard Kipling', 'Orman Çocuğu'),
  level1('book_15_the_wind_in_the_willows', 'The Wind in the Willows', 'Kenneth Grahame', 'Söğütlerdeki Rüzgâr'),
  level1('book_16_peter_pan', 'Peter Pan', 'J. M. Barrie', 'Peter Pan'),
  level1('book_17_the_merry_adventures_of_robin_hood', 'The Merry Adventures of Robin Hood', 'Howard Pyle', "Robin Hood'un Maceraları"),
  level1('book_18_king_arthur', 'King Arthur and the Knights', 'Howard Pyle', 'Kral Arthur'),
  level1('book_19_gullivers_travels', "Gulliver's Travels", 'Jonathan Swift', "Gulliver'in Gezileri"),
  level1('book_20_treasure_island', 'Treasure Island', 'Robert Louis Stevenson', 'Define Adası'),
  level1('book_21_around_the_world_in_eighty_days', 'Around the World in Eighty Days', 'Jules Verne', '80 Günde Devr-i Âlem'),
  level1('book_22_a_christmas_carol', 'A Christmas Carol', 'Charles Dickens', 'Bir Noel Şarkısı'),
  level1('book_23_the_secret_garden', 'The Secret Garden', 'Frances Hodgson Burnett', 'Gizli Bahçe'),
  level1('book_24_white_fang', 'White Fang', 'Jack London', 'Beyaz Diş'),
  level1('book_25_the_time_machine', 'The Time Machine', 'H. G. Wells', 'Zaman Makinesi'),
  level2('book_26_a_scandal_in_bohemia', 'A Scandal in Bohemia', 'Arthur Conan Doyle', "Bohemya'da Skandal"),
  level2('book_27_the_red_headed_league', 'The Red-Headed League', 'Arthur Conan Doyle', 'Kızıl Saçlılar Kulübü'),
  level2('book_28_the_hound_of_the_baskervilles', 'The Hound of the Baskervilles', 'Arthur Conan Doyle', "Baskerville'lerin Köpeği"),
  level2('book_29_the_gift_of_the_magi', 'The Gift of the Magi & The Last Leaf', 'O. Henry', 'Müneccimlerin Hediyesi & Son Yaprak'),
  level2('book_30_the_call_of_the_wild', 'The Call of the Wild', 'Jack London', 'Vahşetin Çağrısı'),
  level2('book_31_frankenstein', 'Frankenstein', 'Mary Shelley', 'Frankenstein'),
  level2('book_32_dracula', 'Dracula', 'Bram Stoker', 'Drakula'),
  level2('book_33_dr_jekyll_and_mr_hyde', 'Dr. Jekyll and Mr. Hyde', 'Robert Louis Stevenson', 'Dr. Jekyll ve Bay Hyde'),
  level2('book_34_the_picture_of_dorian_gray', 'The Picture of Dorian Gray', 'Oscar Wilde', "Dorian Gray'in Portresi"),
  level2('book_35_the_canterville_ghost', 'The Canterville Ghost', 'Oscar Wilde', 'Canterville Hayaleti'),
  level2('book_36_journey_to_the_center_of_the_earth', 'Journey to the Center of the Earth', 'Jules Verne', 'Dünyanın Merkezine Yolculuk'),
  {
    id: 'sample_ch01',
    title: 'The Departure',
    titleTr: 'Demo ders',
    author: 'DictaLearn',
    level: 0,
    pages: 1,
    sentences: 6,
    hasPdf: false,
    kind: 'demo',
  },
  {
    id: 'custom_denme',
    title: 'The Camping Trip',
    titleTr: 'Kamp Gezisi',
    author: 'Kişisel PDF',
    level: 0,
    pages: 1,
    sentences: 23,
    hasPdf: true,
    kind: 'personal',
    pdfFile: 'denme.pdf',
  },
  {
    id: 'custom_a2_flyers',
    title: 'A2 Flyers Picture Vocabulary',
    titleTr: 'Resimli kelime kitabı',
    author: 'Kişisel PDF',
    level: 0,
    pages: 1,
    sentences: 6,
    hasPdf: true,
    kind: 'personal',
    pdfFile: '351851-a2-flyers-wordlist-picture-book.pdf',
  },
]

export const DEFAULT_BOOK_ID = 'book_01_the_happy_prince'

export function findBook(id: string): CatalogBook | undefined {
  return CATALOG.find((b) => b.id === id)
}

export interface LessonAssetUrls {
  jsonUrl: string
  audioUrl: string
  pdfUrl?: string
}

export function lessonAssetUrls(book: CatalogBook, baseUrl: string): LessonAssetUrls {
  const base = baseUrl.endsWith('/') ? baseUrl : `${baseUrl}/`
  const dir = `${base}lessons/${book.id}/`
  return {
    jsonUrl: `${dir}lesson.json`,
    audioUrl: `${dir}audio.mp3`,
    pdfUrl: book.hasPdf ? `${dir}${book.pdfFile ?? `${book.id}.pdf`}` : undefined,
  }
}

export interface CatalogFilter {
  query?: string
  level?: BookLevel | 'all'
}

// Locale-neutral folding so "WILDE", "çağrı" and "cagri" all match.
const foldTurkish = (s: string) =>
  s.toLowerCase().normalize('NFD').replace(/\p{M}/gu, '').replace(/ı/g, 'i')

export function filterCatalog(books: CatalogBook[], filter: CatalogFilter): CatalogBook[] {
  const query = filter.query ? foldTurkish(filter.query.trim()) : ''
  return books.filter((b) => {
    if (filter.level !== undefined && filter.level !== 'all' && b.level !== filter.level) return false
    if (!query) return true
    return [b.title, b.titleTr ?? '', b.author].some((field) => foldTurkish(field).includes(query))
  })
}
