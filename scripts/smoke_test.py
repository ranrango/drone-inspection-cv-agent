from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.app.agent import run_inspection


DEFAULT_SOURCE = "sample_data/sample_detections.json"


def run_smoke_test() -> dict[str, object]:
    result = run_inspection(DEFAULT_SOURCE, min_confidence=0.45)
    events = result["events"]
    high_risk = [item for item in events if item["risk_level"] == "高"]
    return {
        "service": "drone-inspection-cv-agent",
        "status": "ok" if events and high_risk else "failed",
        "source": DEFAULT_SOURCE,
        "used_detections": result["used_detections"],
        "event_count": len(events),
        "overall_risk": result["overall_risk"],
        "has_high_risk_event": bool(high_risk),
    }


def main() -> None:
    print(json.dumps(run_smoke_test(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
