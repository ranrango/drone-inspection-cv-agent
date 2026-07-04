# API 文档

## `GET /health`

返回服务状态。

## `POST /inspect`

请求：

```json
{
  "source": "sample_data/sample_detections.json",
  "min_confidence": 0.45
}
```

响应字段：

| 字段 | 说明 |
|---|---|
| `raw_detections` | 原始检测数量 |
| `used_detections` | 过滤后纳入分析数量 |
| `overall_risk` | 总体风险 |
| `events` | 异常事件列表 |
| `report` | Markdown 巡检报告 |

## `POST /report`

只返回 Markdown 报告。
