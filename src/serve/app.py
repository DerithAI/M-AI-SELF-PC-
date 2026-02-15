from __future__ import annotations

from contextlib import asynccontextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.config import load_settings
from src.model import LinearModel


class PredictRequest(BaseModel):
    features: List[List[float]]


class PredictResponse(BaseModel):
    predictions: List[float]


@dataclass
class ModelState:
    model: LinearModel | None = None
    model_path: Path | None = None


state = ModelState()


def load_model(path: Path) -> LinearModel:
    return LinearModel.load(path)


def create_app() -> FastAPI:
    settings = load_settings()
    model_path = settings.model_dir / "linear_model.json"

    @asynccontextmanager
    async def lifespan(_: FastAPI):
        state.model_path = model_path
        if model_path.exists():
            state.model = load_model(model_path)
        else:
            state.model = None
        yield

    app = FastAPI(title="ML-first inference service", lifespan=lifespan)

    @app.get("/health")
    def health() -> dict[str, str]:
        return {
            "status": "ok",
            "model_path": str(model_path),
            "model_loaded": "yes" if state.model else "no",
        }

    @app.post("/predict", response_model=PredictResponse)
    def predict(request: PredictRequest) -> PredictResponse:
        if state.model is None:
            raise HTTPException(
                status_code=503,
                detail="Model not loaded. Run training first: python -m src.train",
            )
        preds = state.model.predict(request.features)
        return PredictResponse(predictions=preds)

    return app


app = create_app()
