# 部署交付说明

## 本地 API

```bash
pip install -e .
uvicorn src.app.main:app --host 0.0.0.0 --port 8020
```

## Docker

```bash
docker compose up --build
```

## 交付验收命令

本地常规验收：

```bash
make check
```

交付前完整验收：

```bash
make release-check
```

`release-check` 会额外执行 Docker 镜像构建；CI 会执行同样的交付验收命令，确保 API、样例巡检 smoke、代码格式和 Docker 镜像构建都能通过。

只验证容器能启动并通过健康检查：

```bash
make container-check
```

容器内置 Docker `HEALTHCHECK`，`docker compose ps` 可以看到服务健康状态。健康检查访问：

```text
http://127.0.0.1:8020/health
```

## 接入真实模型

1. 在 `detector.py` 中新增 `YoloDetector` 或 `ModelBackend`。
2. 将输入源从 sample JSON 改为图片、视频或抽帧目录。
3. 输出仍然保持统一字段：`frame_id/timestamp/label/confidence/bbox/zone`。
4. 保持 Agent 层不感知具体模型，方便后续替换模型。

## 交付给业务方

- 提供 API 地址、请求示例和字段说明。
- 明确模型版本、置信度阈值、风险区域配置。
- 提供样例巡检报告和异常事件截图。
- 说明告警阈值、人工复核流程和误报处理机制。
