# 评估方案

## 评估目标

这个项目评估的是“CV 检测结果能否转化为业务可用的巡检事件”，因此指标需要覆盖模型、事件聚合和业务告警三层。

## 核心指标

| 指标 | 说明 | 合格标准 |
|---|---|---|
| Detection Precision | 检测框是否准确 | 按模型验证集评估 mAP、Precision、Recall |
| Event Precision | 多帧检测聚合后的事件是否准确 | 同一目标不应重复生成多条高风险告警 |
| Alert Recall | 高风险区域异常是否被发现 | restricted/perimeter/storage 的人员和车辆不漏报 |
| False Alarm Rate | 误报率 | 低置信度、飞鸟、正常维护车辆不应触发高风险 |
| Report Usefulness | 报告是否可直接给业务方 | 包含风险等级、证据帧、区域、时间和处置建议 |

## 样例评测

```json
{
  "source": "sample_data/sample_detections.json",
  "expected_overall_risk": "高",
  "must_have_event": {
    "label": "person",
    "zone": "restricted",
    "risk_level": "高"
  }
}
```

## 失败归因

- 检测漏报：检查模型训练数据、阈值、输入分辨率和小目标增强。
- 重复告警：引入 Track ID、ByteTrack 或 DeepSORT。
- 风险误判：调整区域权重、对象权重和连续出现阈值。
- 报告不可用：增加证据帧、截图链接和人工复核状态。

## 上线监控

- 每日巡检任务数、成功率和平均处理时长。
- GPU 推理耗时、队列积压和失败率。
- 高风险告警人工确认率。
- 误报样本回流数量。
- 模型版本和规则版本变更记录。
