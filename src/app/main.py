from __future__ import annotations

from typing import Dict, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

from .agent import run_inspection

app = FastAPI(title="无人机巡检 CV Agent", version="0.1.0")


class InspectionRequest(BaseModel):
    source: Optional[str] = Field(None, description="检测结果 JSON 路径；为空时使用样例数据")
    min_confidence: float = Field(0.45, ge=0, le=1, description="最低检测置信度")


@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok", "service": "drone-inspection-cv-agent"}


@app.post("/inspect")
def inspect(request: InspectionRequest) -> Dict[str, object]:
    return run_inspection(request.source, min_confidence=request.min_confidence)


@app.post("/report")
def report(request: InspectionRequest) -> Dict[str, str]:
    result = run_inspection(request.source, min_confidence=request.min_confidence)
    return {"report": str(result["report"])}
