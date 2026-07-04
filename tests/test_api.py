from fastapi.testclient import TestClient

from src.app.main import app


client = TestClient(app)


def test_health_endpoint_reports_service_status():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "drone-inspection-cv-agent",
    }


def test_inspect_endpoint_returns_events_and_risk():
    response = client.post(
        "/inspect",
        json={"source": "sample_data/sample_detections.json", "min_confidence": 0.45},
    )

    payload = response.json()
    assert response.status_code == 200
    assert payload["used_detections"] >= 4
    assert payload["overall_risk"] in {"中", "高"}
    assert any(event["risk_level"] == "高" for event in payload["events"])
    assert "无人机巡检分析报告" in payload["report"]


def test_report_endpoint_returns_markdown_report_only():
    response = client.post(
        "/report",
        json={"source": "sample_data/sample_detections.json", "min_confidence": 0.45},
    )

    payload = response.json()
    assert response.status_code == 200
    assert set(payload) == {"report"}
    assert payload["report"].startswith("# 无人机巡检分析报告")
