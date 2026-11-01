# Kawaii Cat Timer

Kawaii Cat Timer is a Windows desktop countdown-widget project built with Python and Tk. Its implementation supports start, pause, reset, direct time entry, keyboard controls, adjustable widget sizes, and remembered local settings.

The project explores a small, approachable timer for focused work or short breaks. Its interface combines a visual countdown with an optional alarm.

## Selected source

[`time_helpers.py`](time_helpers.py) extracts the original `MAX_SECONDS` constant and the `parse_time` and `format_time` functions from `app.py`. The functions are unchanged. They accept whole-minute input or `MM:SS`, check the supported range through `99:59`, and format seconds for display.

This is a small source excerpt, not the complete widget or a release package. Artwork, alarm audio, settings, packaging tools, and executables are outside this showcase. No claim is made here about redistribution rights for the original media. The full widget has not been run or tested as part of publication.
