from __future__ import annotations

import argparse
import json

from .agent import run_inspection


def main() -> None:
    parser = argparse.ArgumentParser(description="无人机巡检 CV Agent")
    parser.add_argument("--source", default="sample_data/sample_detections.json")
    parser.add_argument("--min-confidence", type=float, default=0.45)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    result = run_inspection(args.source, min_confidence=args.min_confidence)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(result["report"])


if __name__ == "__main__":
    main()
