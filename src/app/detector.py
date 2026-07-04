from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

DEFAULT_SAMPLE = Path(__file__).resolve().parents[2] / "sample_data" / "sample_detections.json"


@dataclass(frozen=True)
class Detection:
    frame_id: str
    timestamp: str
    label: str
    confidence: float
    bbox: list[float]
    zone: str


def load_detections(source: str | Path | None = None) -> list[Detection]:
    path = Path(source) if source else DEFAULT_SAMPLE
    payload = json.loads(path.read_text(encoding="utf-8"))
    return [Detection(**item) for item in payload["detections"]]


def filter_detections(detections: list[Detection], min_confidence: float = 0.45) -> list[Detection]:
    return [item for item in detections if item.confidence >= min_confidence]


def group_events(detections: list[Detection]) -> list[dict[str, object]]:
    events: dict[tuple[str, str], dict[str, object]] = {}
    for item in detections:
        key = (item.label, item.zone)
        if key not in events:
            events[key] = {
                "label": item.label,
                "zone": item.zone,
                "count": 0,
                "first_seen": item.timestamp,
                "last_seen": item.timestamp,
                "max_confidence": item.confidence,
                "frames": [],
            }
        event = events[key]
        event["count"] = int(event["count"]) + 1
        event["last_seen"] = item.timestamp
        event["max_confidence"] = max(float(event["max_confidence"]), item.confidence)
        event["frames"].append(item.frame_id)
    return list(events.values())


def score_event(event: dict[str, object]) -> int:
    score = 20
    label = str(event["label"])
    zone = str(event["zone"])
    count = int(event["count"])
    confidence = float(event["max_confidence"])

    if zone in {"restricted", "storage", "perimeter"}:
        score += 30
    if label in {"person", "vehicle", "truck"}:
        score += 20
    if count >= 2:
        score += 15
    if confidence >= 0.8:
        score += 10
    return min(score, 100)


def event_level(score: int) -> str:
    if score >= 75:
        return "高"
    if score >= 50:
        return "中"
    return "低"
