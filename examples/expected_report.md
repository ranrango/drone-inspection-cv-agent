# 无人机巡检分析报告示例

## 核心结论

样例检测结果中，`restricted` 区域连续检测到 `person`，系统应聚合为高风险事件；`perimeter` 和 `storage` 区域的车辆类目标作为中风险事件进入报告。

## 期望检查点

- 原始检测 5 条，过滤后纳入分析 4 条。
- 至少生成 3 个事件。
- `restricted + person` 应为高风险。
- 报告包含总体风险、异常事件和处置建议。

## 演示命令

```bash
python3 -m src.app.cli --source sample_data/sample_detections.json
python3 scripts/smoke_test.py
```
