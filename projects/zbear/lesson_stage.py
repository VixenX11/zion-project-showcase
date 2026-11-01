"""Selected original ZBear lesson-stage definitions; not the complete schema.

The allowed-stage set and Stage definition are unchanged from the original
lesson_plan_schema.py. Imports are limited to those used by this excerpt.
See NOTICE.md for the original rights notice.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


ALLOWED_STAGE_TYPES = {
    "bell_ringer",
    "mini_lesson",
    "guided_practice",
    "cfu_pause",
    "pair_and_share",
    "small_group_activity",
    "independent_practice",
    "exit_ticket",
    "homework",
    "wrap_up",
}


@dataclass
class Stage:
    type: str
    minutes: int = 0
    title: Optional[str] = None
    prompt: Optional[str] = None
    key_points: List[str] = field(default_factory=list)
    materials: List[str] = field(default_factory=list)
    notes: Optional[str] = None

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Stage":
        return Stage(
            type=str(d.get("type", "")).strip(),
            minutes=int(d.get("minutes", 0) or 0),
            title=d.get("title"),
            prompt=d.get("prompt"),
            key_points=list(d.get("key_points", []) or []),
            materials=list(d.get("materials", []) or []),
            notes=d.get("notes"),
        )
