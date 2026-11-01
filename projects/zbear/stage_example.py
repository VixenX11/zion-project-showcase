"""New, offline teaching example using only invented lesson material."""

from dataclasses import asdict
import json

from lesson_stage import Stage


def main():
    fictional_stages = [
        {"type": "mini_lesson", "minutes": 5, "title": "Counting objects"},
        {
            "type": "cfu_pause",
            "minutes": 2,
            "title": "Pause and check understanding",
            "prompt": "Explain how you counted three blocks.",
        },
        {"type": "guided_practice", "minutes": 5, "title": "Try another group"},
    ]
    stages = [Stage.from_dict(item) for item in fictional_stages]
    print(json.dumps([asdict(stage) for stage in stages], indent=2))


if __name__ == "__main__":
    main()
