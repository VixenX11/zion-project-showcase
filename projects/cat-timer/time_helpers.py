MAX_SECONDS = 99 * 60 + 59


def parse_time(value: str) -> int:
    cleaned = value.strip()
    if not cleaned:
        raise ValueError("Please enter a time.")
    if ":" in cleaned:
        pieces = cleaned.split(":")
        if len(pieces) != 2:
            raise ValueError("Use MM:SS, for example 25:00.")
        minutes, seconds = (int(piece.strip()) for piece in pieces)
    else:
        minutes, seconds = int(cleaned), 0
    if minutes < 0 or not 0 <= seconds <= 59:
        raise ValueError("Minutes must be positive and seconds must be from 00 to 59.")
    total = minutes * 60 + seconds
    if not 0 <= total <= MAX_SECONDS:
        raise ValueError("The largest supported time is 99:59.")
    return total


def format_time(total_seconds: int) -> str:
    total_seconds = max(0, min(MAX_SECONDS, int(total_seconds)))
    minutes, seconds = divmod(total_seconds, 60)
    return f"{minutes:02d}:{seconds:02d}"
