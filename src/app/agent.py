from __future__ import annotations

from pathlib import Path

from .detector import event_level, filter_detections, group_events, load_detections, score_event


def run_inspection(
    source: str | Path | None = None, min_confidence: float = 0.45
) -> dict[str, object]:
    raw = load_detections(source)
    detections = filter_detections(raw, min_confidence=min_confidence)
    events = group_events(detections)

    enriched_events = []
    for event in events:
        score = score_event(event)
        enriched_events.append({**event, "risk_score": score, "risk_level": event_level(score)})

    high_events = [item for item in enriched_events if item["risk_level"] == "高"]
    overall = "高" if high_events else "中" if enriched_events else "低"
    report = generate_report(
        raw_count=len(raw), used_count=len(detections), events=enriched_events, overall=overall
    )
    return {
        "source": str(source or "sample_data/sample_detections.json"),
        "raw_detections": len(raw),
        "used_detections": len(detections),
        "overall_risk": overall,
        "events": enriched_events,
        "report": report,
    }


def generate_report(
    raw_count: int, used_count: int, events: list[dict[str, object]], overall: str
) -> str:
    event_lines = []
    for event in sorted(events, key=lambda item: int(item["risk_score"]), reverse=True):
        event_lines.append(
            f"- {event['risk_level']}风险：{event['zone']} 区域发现 {event['label']}，"
            f"出现 {event['count']} 次，最高置信度 {float(event['max_confidence']):.2f}，"
            f"时间 {event['first_seen']} -> {event['last_seen']}。"
        )

    suggestions = [
        "高风险事件优先推送安保人员复核原始视频。",
        "中风险事件进入巡检日报，并与历史同航线结果对比。",
        "低置信度检测结果不直接告警，只作为模型迭代样本。",
    ]

    return "\n".join(
        [
            "# 无人机巡检分析报告",
            "",
            f"## 总体风险：{overall}",
            f"原始检测 {raw_count} 条，过滤后纳入分析 {used_count} 条。",
            "",
            "## 异常事件",
            *(event_lines or ["- 未发现达到阈值的异常事件。"]),
            "",
            "## 处置建议",
            *[f"- {item}" for item in suggestions],
            "",
            "## 工程说明",
            "- 当前检测输入为标准化 detection schema，可替换为 YOLOv8/RT-DETR/GroundingDINO 推理结果。",
            "- 业务层只依赖统一 schema，因此模型升级不会影响 API 调用方。",
        ]
    )
