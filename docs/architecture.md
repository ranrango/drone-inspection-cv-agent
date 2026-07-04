# 架构设计

## 目标

把 CV 检测项目包装成 Agent 工具，使它不只是“识别图片里有什么”，而是能回答“巡检中是否有异常、风险多高、应该怎么处置”。

## 数据流

```text
无人机视频/图片
  -> 抽帧
  -> CV 检测模型
  -> 标准化 detections
  -> 置信度过滤
  -> 事件聚合
  -> 风险评分
  -> 巡检报告
  -> API/前端/告警系统
```

## 模块职责

| 模块 | 职责 | 当前实现 | 生产替换 |
|---|---|---|---|
| Detector Adapter | 把模型输出转成统一 schema | 读取样例 JSON | YOLOv8/RT-DETR/GroundingDINO 推理 |
| Event Builder | 多帧检测合并为事件 | 按 label + zone 聚合 | Track ID + ByteTrack/DeepSORT |
| Risk Engine | 输出风险等级 | 可解释规则 | 业务规则 + 统计模型 |
| Agent Orchestrator | 编排工具链 | 固定流程 | LangGraph / Function Calling |
| Report Generator | 输出巡检报告 | Markdown | PDF/HTML/工单系统 |

## 为什么要封装成 Agent

检测模型输出的是 bbox 和 class，业务方真正需要的是异常事件、风险等级、证据帧和处置建议。Agent 的价值是把模型结果接到业务流程中，并且让模型升级、规则调整、报告输出互相解耦。
