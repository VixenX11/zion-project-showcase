package com.m4mark.app.recording

class RecordingClock {
    private var accumulatedMs: Long = 0
    private var activeSinceMs: Long? = null

    fun start(nowMs: Long) {
        accumulatedMs = 0
        activeSinceMs = nowMs
    }

    fun pause(nowMs: Long): Long {
        accumulatedMs = elapsed(nowMs)
        activeSinceMs = null
        return accumulatedMs
    }

    fun resume(nowMs: Long) {
        if (activeSinceMs == null) activeSinceMs = nowMs
    }

    fun elapsed(nowMs: Long): Long = accumulatedMs + (activeSinceMs?.let { nowMs - it } ?: 0L)

    fun reset() {
        accumulatedMs = 0
        activeSinceMs = null
    }
}
