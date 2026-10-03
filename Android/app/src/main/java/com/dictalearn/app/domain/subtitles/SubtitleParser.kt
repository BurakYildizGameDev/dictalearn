package com.dictalearn.app.domain.subtitles

import com.dictalearn.app.domain.model.Segment

object SubtitleParser {

    private val TIME_ARROW_REGEX = Regex(
        """((?:\d{1,2}:)?\d{2}:\d{2}[,.]\d{1,3})\s*-->\s*((?:\d{1,2}:)?\d{2}:\d{2}[,.]\d{1,3})"""
    )
    private val TAG_REGEX = Regex("""<[^>]+>""")
    private val WHITESPACE_REGEX = Regex("""\s+""")

    fun parseTimestampToMs(timeStr: String): Int {
        val trimmed = timeStr.trim()
        val parts = trimmed.split(Regex("[,.]"))
        val timePart = parts[0]
        val millisPart = if (parts.size > 1) parts[1] else "0"

        val timeTokens = timePart.split(":").map { it.toIntOrNull() ?: 0 }
        var hours = 0
        var minutes = 0
        var seconds = 0

        when (timeTokens.size) {
            3 -> {
                hours = timeTokens[0]
                minutes = timeTokens[1]
                seconds = timeTokens[2]
            }
            2 -> {
                minutes = timeTokens[0]
                seconds = timeTokens[1]
            }
            1 -> {
                seconds = timeTokens[0]
            }
        }

        val normalizedMillisStr = millisPart.padEnd(3, '0').take(3)
        val millis = normalizedMillisStr.toIntOrNull() ?: 0

        return hours * 3600000 + minutes * 60000 + seconds * 1000 + millis
    }

    fun formatMsToTimestamp(ms: Int, format: String = "srt"): String {
        val safeMs = maxOf(0, ms)
        val hours = safeMs / 3600000
        val minutes = (safeMs % 3600000) / 60000
        val seconds = (safeMs % 60000) / 1000
        val millis = safeMs % 1000

        val separator = if (format.lowercase() == "srt") "," else "."
        return String.format("%02d:%02d:%02d%s%03d", hours, minutes, seconds, separator, millis)
    }

    fun cleanSubtitleText(raw: String): String {
        return raw
            .replace(TAG_REGEX, "")
            .replace("&amp;", "&")
            .replace("&lt;", "<")
            .replace("&gt;", ">")
            .replace("&nbsp;", " ")
            .replace("\r\n", " ")
            .replace("\n", " ")
            .replace("\r", " ")
            .replace(WHITESPACE_REGEX, " ")
            .trim()
    }

    fun parseSrt(rawSrt: String): List<Segment> {
        val normalized = rawSrt.replace("\r\n", "\n").replace("\r", "\n")
        val blocks = normalized.split(Regex("""\n\s*\n"""))
        val segments = mutableListOf<Segment>()
        var nextId = 1

        for (block in blocks) {
            val lines = block.lines().map { it.trim() }.filter { it.isNotEmpty() }
            if (lines.isEmpty()) continue

            val timeLineIndex = lines.indexOfFirst { TIME_ARROW_REGEX.containsMatchIn(it) }
            if (timeLineIndex == -1) continue

            val match = TIME_ARROW_REGEX.find(lines[timeLineIndex]) ?: continue
            val startMs = parseTimestampToMs(match.groupValues[1])
            val endMs = parseTimestampToMs(match.groupValues[2])

            if (endMs <= startMs) continue

            val textLines = lines.subList(timeLineIndex + 1, lines.size)
            val text = cleanSubtitleText(textLines.joinToString(" "))
            if (text.isEmpty()) continue

            segments.add(
                Segment(
                    id = nextId++,
                    startMs = startMs,
                    endMs = endMs,
                    text = text
                )
            )
        }

        return segments
    }

    fun parseVtt(rawVtt: String): List<Segment> {
        val normalized = rawVtt.replace("\r\n", "\n").replace("\r", "\n")
        val blocks = normalized.split(Regex("""\n\s*\n"""))
        val segments = mutableListOf<Segment>()
        var nextId = 1

        for (block in blocks) {
            val lines = block.lines().map { it.trim() }.filter { it.isNotEmpty() }
            if (lines.isEmpty()) continue

            if (lines[0].startsWith("WEBVTT") || lines[0].startsWith("NOTE") || lines[0].startsWith("STYLE")) {
                continue
            }

            val timeLineIndex = lines.indexOfFirst { TIME_ARROW_REGEX.containsMatchIn(it) }
            if (timeLineIndex == -1) continue

            val match = TIME_ARROW_REGEX.find(lines[timeLineIndex]) ?: continue
            val startMs = parseTimestampToMs(match.groupValues[1])
            val endMs = parseTimestampToMs(match.groupValues[2])

            if (endMs <= startMs) continue

            val textLines = lines.subList(timeLineIndex + 1, lines.size)
            val text = cleanSubtitleText(textLines.joinToString(" "))
            if (text.isEmpty()) continue

            segments.add(
                Segment(
                    id = nextId++,
                    startMs = startMs,
                    endMs = endMs,
                    text = text
                )
            )
        }

        return segments
    }

    fun parseSubtitles(content: String): List<Segment> {
        return if (content.trim().startsWith("WEBVTT")) {
            parseVtt(content)
        } else {
            parseSrt(content)
        }
    }
}
