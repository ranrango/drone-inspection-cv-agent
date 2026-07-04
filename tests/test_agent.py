from src.app.agent import run_inspection


def test_run_inspection_detects_high_risk_event():
    result = run_inspection("sample_data/sample_detections.json")
    assert result["used_detections"] >= 4
    assert result["overall_risk"] in {"中", "高"}
    assert any(event["risk_level"] == "高" for event in result["events"])
    assert "无人机巡检分析报告" in result["report"]
