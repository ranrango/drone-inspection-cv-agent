# v0.1.0 Release Notes

## Highlights

- 将无人机检测结果包装成可交付 CV Agent：检测结果过滤、事件聚合、风险评分、巡检报告。
- 提供 CLI、FastAPI、Docker、docker-compose、Makefile 和 smoke test。
- README 增加架构图和 smoke 输出图，便于 GitHub 展示和面试讲解。
- 文档包含 API、部署、复现、评估方案、路线图和面试讲述稿。

## Verification

```bash
python3 -m pytest tests/ -q
python3 scripts/smoke_test.py
```

期望 smoke 输出包含：

- `status: ok`
- `used_detections: 4`
- `event_count: 3`
- `overall_risk: 高`

## Next

- 接入真实 YOLOv8 / RT-DETR 推理后端。
- 支持图片目录、视频抽帧和证据帧输出。
- 引入 Track ID、ByteTrack/DeepSORT 做事件归并。
- 对接告警工单、人工复核和误报反馈闭环。
