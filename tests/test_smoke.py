from scripts.smoke_test import run_smoke_test
import json
import subprocess
import sys
from pathlib import Path


def test_smoke_test_returns_core_fields():
    result = run_smoke_test()
    assert result["service"] == "drone-inspection-cv-agent"
    assert result["status"] == "ok"
    assert result["event_count"] >= 1
    assert result["overall_risk"] in {"低", "中", "高"}
    assert result["has_high_risk_event"] is True


def test_smoke_script_can_run_as_cli():
    repo_root = Path(__file__).resolve().parents[1]
    completed = subprocess.run(
        [sys.executable, "scripts/smoke_test.py"],
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(completed.stdout)
    assert payload["status"] == "ok"
