from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from src.config import load_settings
from src.model import LinearModel


class PredictRequest(BaseModel):
    features: List[List[float]]


class PredictResponse(BaseModel):
    predictions: List[float]


@dataclass
class ModelState:
    model: LinearModel


def load_model(path: Path) -> LinearModel:
    return LinearModel.load(path)


def create_app() -> FastAPI:
    settings = load_settings()
    model_path = settings.model_dir / "linear_model.json"
    state = ModelState(model=load_model(model_path))

    app = FastAPI(title="ML-first inference service")

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "model": model_path.name}

    @app.post("/predict", response_model=PredictResponse)
    def predict(request: PredictRequest) -> PredictResponse:
        preds = state.model.predict(request.features)
        return PredictResponse(predictions=preds)

    return app


app = create_app()
