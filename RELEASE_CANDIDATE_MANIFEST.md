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
- `scripts/*.py`
- `examples/*`
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

## Post-Release Improvements

- 增加 `scripts/smoke_test.py` 一键自检。
- 增加 examples、评估方案和路线图文档。
- README 增加预期输出和项目展示说明。
