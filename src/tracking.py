from __future__ import annotations

from pathlib import Path
from typing import Any


class BaseTracker:
    def log_params(self, params: dict[str, Any]) -> None:  # pragma: no cover - interface
        raise NotImplementedError

    def log_metrics(self, metrics: dict[str, float]) -> None:  # pragma: no cover - interface
        raise NotImplementedError

    def log_artifact(self, path: Path) -> None:  # pragma: no cover - interface
        raise NotImplementedError

    def close(self) -> None:  # pragma: no cover - interface
        raise NotImplementedError


class NoopTracker(BaseTracker):
    def log_params(self, params: dict[str, Any]) -> None:
        _ = params

    def log_metrics(self, metrics: dict[str, float]) -> None:
        _ = metrics

    def log_artifact(self, path: Path) -> None:
        _ = path

    def close(self) -> None:
        return None


class MlflowTracker(BaseTracker):
    def __init__(self, tracking_uri: str, experiment_name: str, run_name: str) -> None:
        import mlflow

        self._mlflow = mlflow
        self._mlflow.set_tracking_uri(tracking_uri)
        self._mlflow.set_experiment(experiment_name)
        self._run = self._mlflow.start_run(run_name=run_name)

    def log_params(self, params: dict[str, Any]) -> None:
        self._mlflow.log_params(params)

    def log_metrics(self, metrics: dict[str, float]) -> None:
        self._mlflow.log_metrics(metrics)

    def log_artifact(self, path: Path) -> None:
        self._mlflow.log_artifact(str(path))

    def close(self) -> None:
        self._mlflow.end_run()


def build_tracker(tracking_uri: str, experiment_name: str, run_name: str) -> BaseTracker:
    try:
        return MlflowTracker(
            tracking_uri=tracking_uri,
            experiment_name=experiment_name,
            run_name=run_name,
        )
    except Exception:
        return NoopTracker()
