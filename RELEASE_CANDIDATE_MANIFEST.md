# Release Candidate Manifest

Generated: 2026-07-04

## Included

- `README.md`
- `pyproject.toml`
- `Makefile`
- `Dockerfile`
- `docker-compose.yml`
- `.env.example`
- `.gitignore`
- `src/app/*.py`
- `sample_data/*.json`
- `tests/*.py`
- `docs/*.md`
- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `LICENSE`

## Intentionally Excluded

- `.env`
- 真实视频、图片和巡检日志
- 模型权重：`*.pt`, `*.onnx`, `*.engine`
- GPU 推理缓存和大文件输出

## Release Notes

本版本用于展示“CV 模型如何包装成 Agent 工具”。默认不包含真实模型权重，便于开源和面试演示。
