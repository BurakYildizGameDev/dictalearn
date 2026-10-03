package com.dictalearn.app.domain

import com.dictalearn.app.domain.subtitles.SubtitleParser
import org.junit.Assert.*
import org.junit.Test

class SubtitleParserTest {

    @Test
    fun parseTimestampToMs_parsesSrtAndVttFormats() {
        assertEquals(1000, SubtitleParser.parseTimestampToMs("00:00:01,000"))
        assertEquals(83456, SubtitleParser.parseTimestampToMs("00:01:23,456"))
        assertEquals(3600000, SubtitleParser.parseTimestampToMs("01:00:00,000"))

        assertEquals(1500, SubtitleParser.parseTimestampToMs("00:00:01.500"))
        assertEquals(83456, SubtitleParser.parseTimestampToMs("01:23.456"))
    }

    @Test
    fun formatMsToTimestamp_formatsCorrectly() {
        assertEquals("00:01:23,456", SubtitleParser.formatMsToTimestamp(83456, "srt"))
        assertEquals("00:01:23.456", SubtitleParser.formatMsToTimestamp(83456, "vtt"))
    }

    @Test
    fun cleanSubtitleText_stripsTagsAndNormalizes() {
        val raw = "<i>Hello</i>, <b>world</b>! &amp; welcome &lt;here&gt;"
        assertEquals("Hello, world! & welcome <here>", SubtitleParser.cleanSubtitleText(raw))
    }

    @Test
    fun parseSrt_parsesStandardContent() {
        val srt = """
            1
            00:00:00,500 --> 00:00:04,200
            He packed his small brown suitcase.

            2
            00:00:04,500 --> 00:00:08,100
            The morning cold hit him immediately.
        """.trimIndent()

        val segments = SubtitleParser.parseSrt(srt)
        assertEquals(2, segments.size)
        assertEquals(1, segments[0].id)
        assertEquals(500, segments[0].startMs)
        assertEquals(4200, segments[0].endMs)
        assertEquals("He packed his small brown suitcase.", segments[0].text)

        assertEquals(2, segments[1].id)
        assertEquals(4500, segments[1].startMs)
        assertEquals(8100, segments[1].endMs)
        assertEquals("The morning cold hit him immediately.", segments[1].text)
    }

    @Test
    fun parseVtt_parsesStandardContentWithHeader() {
        val vtt = """
            WEBVTT - Departure

            00:00:01.000 --> 00:00:04.000
            He packed his small brown suitcase.

            NOTE comment

            00:04.500 --> 00:08.000
            The morning cold hit him.
        """.trimIndent()

        val segments = SubtitleParser.parseVtt(vtt)
        assertEquals(2, segments.size)
        assertEquals(1000, segments[0].startMs)
        assertEquals(4000, segments[0].endMs)
        assertEquals(4500, segments[1].startMs)
        assertEquals(8000, segments[1].endMs)
    }

    @Test
    fun parseSubtitles_autoDetectsFormat() {
        val vtt = "WEBVTT\n\n00:00:01.000 --> 00:00:03.000\nHello VTT!"
        val srt = "1\n00:00:01,000 --> 00:00:03,000\nHello SRT!"

        val vttRes = SubtitleParser.parseSubtitles(vtt)
        val srtRes = SubtitleParser.parseSubtitles(srt)

        assertEquals("Hello VTT!", vttRes[0].text)
        assertEquals("Hello SRT!", srtRes[0].text)
    }
}
