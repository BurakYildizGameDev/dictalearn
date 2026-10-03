import React, { useState, useRef } from 'react'
import type { Lesson, Segment } from '../domain/lessons/types'
import type { AudioEngine } from '../domain/audio/audio-engine'
import { validateLesson } from '../domain/lessons/lesson-validator'
import { parseSubtitles, formatMsToTimestamp } from '../domain/subtitles/subtitle-parser'
import { downloadLessonZip, importLessonZip } from '../domain/packages/lesson-package'
import {
  Play,
  Trash2,
  Plus,
  Upload,
  Download,
  Music,
  FileArchive,
  ArrowLeft,
  CheckCircle,
  AlertCircle,
  FileText,
} from 'lucide-react'

export interface LessonEditorViewProps {
  audioEngine: AudioEngine
  initialLesson?: Lesson | null
  onStartLesson: (lesson: Lesson, audioUrl: string) => void
  onCancel: () => void
}

export const LessonEditorView: React.FC<LessonEditorViewProps> = ({
  audioEngine,
  initialLesson,
  onStartLesson,
  onCancel,
}) => {
  const [title, setTitle] = useState(initialLesson?.title || 'Yeni Ders')
  const [lessonId, setLessonId] = useState(initialLesson?.lesson_id || 'custom_lesson_01')
  const [sourceLang, setSourceLang] = useState(initialLesson?.source_lang || 'en')
  const [targetLang, setTargetLang] = useState(initialLesson?.target_lang || 'tr')
  const [audioFileName, setAudioFileName] = useState(initialLesson?.audio_file || 'audio.wav')
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null)
  const [audioUrl, setAudioUrl] = useState<string | null>(null)
  const [segments, setSegments] = useState<Segment[]>(
    initialLesson?.segments || [
      {
        id: 1,
        start_ms: 0,
        end_ms: 3000,
        text: 'Type your first English sentence here.',
        translation: 'İlk cümlenizin Türkçe çevirisini buraya yazın.',
      },
    ]
  )

  const [validationErrors, setValidationErrors] = useState<string[]>([])
  const [statusMessage, setStatusMessage] = useState<string | null>(null)

  const srtInputRef = useRef<HTMLInputElement>(null)
  const zipInputRef = useRef<HTMLInputElement>(null)
  const audioInputRef = useRef<HTMLInputElement>(null)

  // Handle audio file selection
  const handleAudioSelected = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return

    setAudioBlob(file)
    setAudioFileName(file.name)
    const url = URL.createObjectURL(file)
    setAudioUrl(url)

    try {
      await audioEngine.load(url)
      setStatusMessage(`Ses dosyası yüklendi: ${file.name}`)
    } catch {
      setStatusMessage(`Ses yüklenirken uyarı oluştu.`)
    }
  }

  // Handle SRT or VTT file import
  const handleSubtitleFileSelected = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return

    try {
      const text = await file.text()
      const parsed = parseSubtitles(text)
      if (parsed.length === 0) {
        setValidationErrors(['Altyazı dosyasından geçerli segment çıkarılamadı.'])
        return
      }

      setSegments(parsed)
      setStatusMessage(`${parsed.length} cümle altyazıdan başarıyla aktarıldı!`)
      setValidationErrors([])
    } catch (err: unknown) {
      const msg = err instanceof Error ? err.message : 'Altyazı ayrıştırılamadı.'
      setValidationErrors([msg])
    }
  }

  // Handle Zip file import
  const handleZipFileSelected = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return

    try {
      setStatusMessage('Zip paketi açılıyor...')
      const imported = await importLessonZip(file)
      setTitle(imported.lesson.title)
      setLessonId(imported.lesson.lesson_id)
      setSourceLang(imported.lesson.source_lang)
      setTargetLang(imported.lesson.target_lang)
      setAudioFileName(imported.lesson.audio_file)
      setSegments(imported.lesson.segments)
      setAudioBlob(imported.audioBlob)
      setAudioUrl(imported.audioUrl)

      await audioEngine.load(imported.audioUrl)
      setStatusMessage(`Zip paketi başarıyla yüklendi: "${imported.lesson.title}" (${imported.lesson.segments.length} segment)`)
      setValidationErrors([])
    } catch (err: unknown) {
      const msg = err instanceof Error ? err.message : 'Zip paketi yüklenemedi.'
      setValidationErrors([msg])
    }
  }

  // Update single segment
  const updateSegment = (index: number, updates: Partial<Segment>) => {
    setSegments((prev) => {
      const copy = [...prev]
      copy[index] = { ...copy[index], ...updates }
      return copy
    })
  }

  // Add new segment
  const addSegment = () => {
    setSegments((prev) => {
      const last = prev[prev.length - 1]
      const nextStart = last ? last.end_ms + 200 : 0
      const nextEnd = nextStart + 3000
      return [
        ...prev,
        {
          id: prev.length + 1,
          start_ms: nextStart,
          end_ms: nextEnd,
          text: '',
          translation: '',
        },
      ]
    })
  }

  // Remove segment
  const removeSegment = (index: number) => {
    if (segments.length <= 1) {
      alert('Derste en az 1 segment bulunmalıdır.')
      return
    }
    setSegments((prev) => {
      const filtered = prev.filter((_, i) => i !== index)
      // re-index IDs sequentially
      return filtered.map((seg, i) => ({ ...seg, id: i + 1 }))
    })
  }

  // Play segment range
  const playSegmentAudio = (startMs: number, endMs: number) => {
    if (!audioUrl) {
      alert('Lütfen önce bir ses dosyası seçin.')
      return
    }
    audioEngine.playRange(startMs, endMs).catch(() => {})
  }

  // Build lesson object
  const buildLesson = (): Lesson => {
    return {
      schema_version: 1,
      lesson_id: lessonId.trim() || 'custom_lesson',
      title: title.trim() || 'İsimsiz Ders',
      source_lang: sourceLang,
      target_lang: targetLang,
      audio_file: audioFileName || 'audio.wav',
      segments: segments.map((seg, i) => ({
        ...seg,
        id: i + 1,
        text: seg.text.trim(),
        translation: seg.translation?.trim() || undefined,
        notes: seg.notes?.trim() || undefined,
      })),
    }
  }

  // Handle Export to Zip
  const handleExportZip = async () => {
    const lesson = buildLesson()
    const validation = validateLesson(lesson)
    if (!validation.isValid) {
      setValidationErrors(validation.errors)
      return
    }

    if (!audioBlob) {
      setValidationErrors(['Zip olarak dışa aktarmak için bir ses dosyası seçmelisiniz.'])
      return
    }

    try {
      await downloadLessonZip(lesson, audioBlob)
      setStatusMessage(`Ders "${lesson.lesson_id}.zip" olarak indirildi!`)
      setValidationErrors([])
    } catch (err: unknown) {
      const msg = err instanceof Error ? err.message : 'Dışa aktarma başarısız oldu.'
      setValidationErrors([msg])
    }
  }

  // Handle Save and Start
  const handleSaveAndStart = () => {
    const lesson = buildLesson()
    const validation = validateLesson(lesson)
    if (!validation.isValid) {
      setValidationErrors(validation.errors)
      return
    }

    if (!audioUrl) {
      setValidationErrors(['Dersi başlatmak için bir ses dosyası seçmelisiniz.'])
      return
    }

    onStartLesson(lesson, audioUrl)
  }

  return (
    <div className="max-w-4xl mx-auto w-full px-4 py-6 space-y-6">
      {/* Top Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-800">
        <div className="flex items-center gap-3">
          <button
            onClick={onCancel}
            className="p-2 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg transition cursor-pointer"
            title="Geri Dön"
          >
            <ArrowLeft className="w-4 h-4" />
          </button>
          <div>
            <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2">
              <FileText className="w-5 h-5 text-indigo-400" />
              <span>Ders Oluşturucu & Düzenleyici</span>
            </h1>
            <p className="text-xs text-slate-400">
              Kendi sesinizi ve altyazılarınızı ekleyerek anında özel dersler oluşturun.
            </p>
          </div>
        </div>

        {/* Quick Import Buttons */}
        <div className="flex items-center gap-2">
          {/* Import Subtitles */}
          <input
            ref={srtInputRef}
            type="file"
            accept=".srt,.vtt,text/plain"
            onChange={handleSubtitleFileSelected}
            className="hidden"
          />
          <button
            type="button"
            onClick={() => srtInputRef.current?.click()}
            className="flex items-center gap-1.5 px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg text-xs font-medium border border-slate-700 transition cursor-pointer"
          >
            <Upload className="w-3.5 h-3.5 text-indigo-400" />
            <span>SRT / VTT Yükle</span>
          </button>

          {/* Import Zip */}
          <input
            ref={zipInputRef}
            type="file"
            accept=".zip"
            onChange={handleZipFileSelected}
            className="hidden"
          />
          <button
            type="button"
            onClick={() => zipInputRef.current?.click()}
            className="flex items-center gap-1.5 px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg text-xs font-medium border border-slate-700 transition cursor-pointer"
          >
            <FileArchive className="w-3.5 h-3.5 text-amber-400" />
            <span>.Zip İçe Aktar</span>
          </button>
        </div>
      </div>

      {/* Notifications / Errors */}
      {statusMessage && (
        <div className="p-3 bg-indigo-950/40 border border-indigo-800/60 rounded-xl text-xs text-indigo-300 flex items-center justify-between">
          <span className="flex items-center gap-2">
            <CheckCircle className="w-4 h-4 text-emerald-400" />
            <span>{statusMessage}</span>
          </span>
          <button onClick={() => setStatusMessage(null)} className="text-slate-400 hover:text-white">✕</button>
        </div>
      )}

      {validationErrors.length > 0 && (
        <div className="p-4 bg-rose-950/40 border border-rose-800/60 rounded-xl text-xs text-rose-300 space-y-1">
          <div className="font-semibold flex items-center gap-1.5 text-rose-200">
            <AlertCircle className="w-4 h-4 text-rose-400" />
            <span>Lütfen hataları düzeltin:</span>
          </div>
          <ul className="list-disc list-inside space-y-0.5">
            {validationErrors.map((err, i) => (
              <li key={i}>{err}</li>
            ))}
          </ul>
        </div>
      )}

      {/* SECTION 1: Lesson Metadata */}
      <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-5 space-y-4">
        <h2 className="text-sm font-semibold text-slate-200 uppercase tracking-wider">
          1. Ders Bilgileri & Ses
        </h2>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div className="space-y-1">
            <label className="text-xs text-slate-400">Ders Başlığı</label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="Örn: Chapter 1: The Departure"
              className="w-full bg-slate-950 border border-slate-700 rounded-lg p-2.5 text-sm text-slate-100 focus:outline-none focus:border-indigo-500"
            />
          </div>

          <div className="space-y-1">
            <label className="text-xs text-slate-400">Ders Kimliği (ID)</label>
            <input
              type="text"
              value={lessonId}
              onChange={(e) => setLessonId(e.target.value)}
              placeholder="Örn: ch01_departure"
              className="w-full bg-slate-950 border border-slate-700 rounded-lg p-2.5 text-sm text-slate-100 font-mono focus:outline-none focus:border-indigo-500"
            />
          </div>
        </div>

        {/* Audio File Selection */}
        <div className="pt-2 border-t border-slate-800/80 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-lg bg-indigo-600/20 text-indigo-400 flex items-center justify-center">
              <Music className="w-4 h-4" />
            </div>
            <div>
              <span className="text-xs text-slate-300 font-medium block">
                {audioFileName ? audioFileName : 'Ses dosyası seçilmedi'}
              </span>
              <span className="text-[11px] text-slate-500">
                {audioUrl ? 'Ses hazır ve dinlenebilir' : '.wav veya .mp3 yükleyin'}
              </span>
            </div>
          </div>

          <input
            ref={audioInputRef}
            type="file"
            accept="audio/*"
            onChange={handleAudioSelected}
            className="hidden"
          />
          <button
            type="button"
            onClick={() => audioInputRef.current?.click()}
            className="px-3.5 py-2 bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg text-xs font-medium transition cursor-pointer"
          >
            Ses Dosyası Seç (.wav / .mp3)
          </button>
        </div>
      </div>

      {/* SECTION 2: Segments List Editor */}
      <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-5 space-y-4">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-sm font-semibold text-slate-200 uppercase tracking-wider">
              2. Cümleler / Segmentler ({segments.length})
            </h2>
            <p className="text-xs text-slate-400 mt-0.5">
              Her cümlenin ses başlangıç/bitiş zamanını ve metnini belirleyin.
            </p>
          </div>

          <button
            type="button"
            onClick={addSegment}
            className="flex items-center gap-1.5 px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg text-xs font-medium transition cursor-pointer shadow-sm"
          >
            <Plus className="w-3.5 h-3.5" />
            <span>Yeni Cümle Ekle</span>
          </button>
        </div>

        <div className="space-y-3">
          {segments.map((seg, idx) => (
            <div
              key={seg.id || idx}
              className="bg-slate-950/60 border border-slate-800 hover:border-slate-700 rounded-xl p-4 space-y-3 transition"
            >
              <div className="flex items-center justify-between border-b border-slate-800/60 pb-2">
                <span className="text-xs font-bold text-indigo-400">
                  Cümle #{idx + 1}
                </span>

                <div className="flex items-center gap-2">
                  {/* Play Segment Button */}
                  <button
                    type="button"
                    onClick={() => playSegmentAudio(seg.start_ms, seg.end_ms)}
                    disabled={!audioUrl}
                    className="flex items-center gap-1 px-2.5 py-1 bg-indigo-950/60 hover:bg-indigo-900/80 disabled:opacity-30 text-indigo-300 border border-indigo-800/50 rounded text-xs transition cursor-pointer"
                    title="Segmenti Çal"
                  >
                    <Play className="w-3 h-3" />
                    <span>Test Et</span>
                  </button>

                  {/* Delete Button */}
                  <button
                    type="button"
                    onClick={() => removeSegment(idx)}
                    className="p-1 text-slate-500 hover:text-rose-400 transition cursor-pointer"
                    title="Cümleyi Sil"
                  >
                    <Trash2 className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>

              {/* Times Row */}
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
                <div>
                  <label className="text-slate-400 block mb-1">Başlangıç (ms)</label>
                  <input
                    type="number"
                    value={seg.start_ms}
                    onChange={(e) => updateSegment(idx, { start_ms: parseInt(e.target.value, 10) || 0 })}
                    className="w-full bg-slate-900 border border-slate-700 rounded px-2.5 py-1.5 text-slate-100 font-mono"
                  />
                  <span className="text-[10px] text-slate-500 block mt-0.5">
                    {formatMsToTimestamp(seg.start_ms, 'vtt')}
                  </span>
                </div>

                <div>
                  <label className="text-slate-400 block mb-1">Bitiş (ms)</label>
                  <input
                    type="number"
                    value={seg.end_ms}
                    onChange={(e) => updateSegment(idx, { end_ms: parseInt(e.target.value, 10) || 0 })}
                    className="w-full bg-slate-900 border border-slate-700 rounded px-2.5 py-1.5 text-slate-100 font-mono"
                  />
                  <span className="text-[10px] text-slate-500 block mt-0.5">
                    {formatMsToTimestamp(seg.end_ms, 'vtt')}
                  </span>
                </div>

                <div className="col-span-2">
                  <label className="text-slate-400 block mb-1">Süre</label>
                  <span className="text-xs text-indigo-300 font-mono inline-block py-1.5">
                    {Math.max(0, (seg.end_ms - seg.start_ms) / 1000).toFixed(2)} saniye
                  </span>
                </div>
              </div>

              {/* Text Fields */}
              <div className="space-y-2">
                <div>
                  <label className="text-xs text-slate-300 block mb-1 font-medium">
                    İngilizce Metin:
                  </label>
                  <textarea
                    rows={2}
                    value={seg.text}
                    onChange={(e) => updateSegment(idx, { text: e.target.value })}
                    placeholder="He packed his small brown suitcase..."
                    className="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-sm text-slate-100 focus:outline-none focus:border-indigo-500 resize-none font-sans"
                  />
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div>
                    <label className="text-xs text-slate-400 block mb-1">
                      Türkçe Çeviri (İsteğe bağlı):
                    </label>
                    <input
                      type="text"
                      value={seg.translation || ''}
                      onChange={(e) => updateSegment(idx, { translation: e.target.value })}
                      placeholder="Küçük kahverengi bavulunu topladı..."
                      className="w-full bg-slate-900 border border-slate-700 rounded px-2.5 py-1.5 text-xs text-slate-200 focus:outline-none focus:border-indigo-500"
                    />
                  </div>

                  <div>
                    <label className="text-xs text-slate-400 block mb-1">
                      Not (İsteğe bağlı):
                    </label>
                    <input
                      type="text"
                      value={seg.notes || ''}
                      onChange={(e) => updateSegment(idx, { notes: e.target.value })}
                      placeholder="Gramer veya kelime ipucu..."
                      className="w-full bg-slate-900 border border-slate-700 rounded px-2.5 py-1.5 text-xs text-slate-200 focus:outline-none focus:border-indigo-500"
                    />
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Action Footer */}
      <div className="flex flex-col sm:flex-row items-center justify-between gap-4 pt-4 border-t border-slate-800">
        <button
          type="button"
          onClick={handleExportZip}
          disabled={!audioBlob}
          className="flex items-center gap-2 px-5 py-2.5 bg-slate-800 hover:bg-slate-700 disabled:opacity-40 text-slate-200 rounded-lg text-sm font-medium border border-slate-700 transition cursor-pointer w-full sm:w-auto justify-center"
          title={!audioBlob ? 'Dışa aktarmak için önce ses dosyası seçin' : ''}
        >
          <Download className="w-4 h-4 text-amber-400" />
          <span>Zip Paketi Olarak İndir</span>
        </button>

        <div className="flex items-center gap-3 w-full sm:w-auto justify-end">
          <button
            type="button"
            onClick={onCancel}
            className="px-5 py-2.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg text-sm font-medium transition cursor-pointer"
          >
            İptal
          </button>

          <button
            type="button"
            onClick={handleSaveAndStart}
            className="flex items-center gap-2 px-6 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg text-sm font-medium transition shadow-sm cursor-pointer"
          >
            <Play className="w-4 h-4" />
            <span>Dersi Başlat</span>
          </button>
        </div>
      </div>
    </div>
  )
}
