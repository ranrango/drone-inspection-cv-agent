PYTHON ?= python3
PORT ?= 8020

.PHONY: help install install-dev install-cv check release-check run api smoke test lint format docker-build docker-run

help:
	@echo "可用命令："
	@echo "  install      安装运行依赖"
	@echo "  install-dev  安装开发依赖"
	@echo "  install-cv   安装真实 CV 推理依赖"
	@echo "  run          运行样例巡检"
	@echo "  api          启动 FastAPI 服务"
	@echo "  check        本地常规验收"
	@echo "  release-check 交付验收，包含 Docker 构建"
	@echo "  smoke        运行一键自检"
	@echo "  test         运行测试"
	@echo "  lint         运行 ruff 检查"
	@echo "  format       运行 black 格式检查"
	@echo "  docker-build 构建镜像"
	@echo "  docker-run   运行容器"

install:
	$(PYTHON) -m pip install -e .

install-dev:
	$(PYTHON) -m pip install -e ".[dev]"

install-cv:
	$(PYTHON) -m pip install -e ".[dev,cv]"

check: test smoke lint format

release-check: check docker-build

run:
	$(PYTHON) -m src.app.cli --source sample_data/sample_detections.json

api:
	uvicorn src.app.main:app --reload --port $(PORT)

smoke:
	$(PYTHON) scripts/smoke_test.py

test:
	$(PYTHON) -m pytest tests/ --tb=short -q

lint:
	ruff check src/ scripts/ tests/

format:
	black --check src/ scripts/ tests/

docker-build:
	docker build -t drone-inspection-cv-agent:latest .

docker-run:
	docker run --rm -p $(PORT):8020 drone-inspection-cv-agent:latest
