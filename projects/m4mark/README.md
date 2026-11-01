# M4Mark

M4Mark is an Android recording and transcription project designed around local storage and deliberate user actions. Its implementation includes microphone recording, pause and resume, recording controls in a foreground service, and manual on-device transcription using whisper.cpp. Audio and Markdown transcripts have separate storage and export controls.

For meeting notes, interviews, or field observations, the design explores keeping recording and transcription on the device while letting the user choose when to transcribe or share a file.

## Selected source

[`RecordingClock.kt`](RecordingClock.kt) is a small, unchanged source excerpt from `app/src/main/java/com/m4mark/app/recording/RecordingClock.kt`. It accumulates active recording time across pauses using caller-supplied millisecond values. Paused time does not increase the recorded duration. The caller remains responsible for providing a suitable clock and coordinating recording state.

This excerpt shows one implementation detail. It is not the Android application, a buildable app package, or a release download. The recording service, user interface, storage, transcription integration, models, and dependencies are outside this showcase. These files have been inspected for this showcase; the full application has not been rebuilt or tested as part of publication.

The original transcription integration uses third-party whisper.cpp code; that engine and its source are not included here.
