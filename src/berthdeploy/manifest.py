"""Berth manifest totals, deployed per environment."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Slot:
    berth: str
    teu: int
    reefer: bool


FLEET = [
    Slot("B1", 2550, False),
    Slot("B2", 3800, True), 
    Slot("B3", 1600, True),
]


def total_teu(slots=None) -> int:
    return sum(s.teu for s in (slots if slots is not None else FLEET))


def reefer_share(slots=None) -> float:
    rows = slots if slots is not None else FLEET
    if not rows:
        return 0.0
    hot = sum(s.teu for s in rows if s.reefer)
    return round(hot / total_teu(rows), 4)


def manifest() -> dict:
    return {
        "berths": len(FLEET),
        "total_teu": total_teu(),
        "reefer_share": reefer_share(),
    }
