# 复现指南

## 1. 运行样例巡检

```bash
python3 -m src.app.cli --source sample_data/sample_detections.json --json
```

## 2. 运行测试

```bash
python3 -m pytest tests/ -q
```

## 3. 启动 API

```bash
pip install -e ".[dev]"
uvicorn src.app.main:app --reload --port 8020
```

## 4. 预期结果

样例数据中 restricted 区域存在 person，多帧重复出现，应被判定为高风险事件。
