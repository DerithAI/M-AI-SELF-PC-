from pathlib import Path

from fastapi.testclient import TestClient

from src.model import LinearModel
from src.serve.app import create_app, state


def test_health_and_predict_flow(tmp_path: Path, monkeypatch) -> None:
    model_path = tmp_path / "linear_model.json"
    LinearModel(weights=[1.0, 2.0], bias=0.5).save(model_path)

    monkeypatch.setenv("MODEL_DIR", str(tmp_path))

    app = create_app()
    with TestClient(app) as client:
        health = client.get("/health")
        assert health.status_code == 200
        assert health.json()["model_loaded"] == "yes"

        response = client.post("/predict", json={"features": [[1, 2], [3, 4]]})
        assert response.status_code == 200
        assert response.json()["predictions"] == [5.5, 11.5]


def test_predict_without_model_returns_503(tmp_path: Path, monkeypatch) -> None:
    state.model = None
    monkeypatch.setenv("MODEL_DIR", str(tmp_path))

    app = create_app()
    with TestClient(app) as client:
        response = client.post("/predict", json={"features": [[1, 2]]})
        assert response.status_code == 503


def test_predict_rejects_rows_with_wrong_feature_count(tmp_path: Path, monkeypatch) -> None:
    model_path = tmp_path / "linear_model.json"
    LinearModel(weights=[1.0, 2.0], bias=0.5).save(model_path)

    monkeypatch.setenv("MODEL_DIR", str(tmp_path))

    app = create_app()
    with TestClient(app) as client:
        response = client.post("/predict", json={"features": [[1], [2, 3, 4]]})
        assert response.status_code == 400
        assert response.json()["detail"] == "Expected 2 features, received 1."
