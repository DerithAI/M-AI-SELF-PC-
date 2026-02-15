from __future__ import annotations

from src.config import load_settings
from src.data import load_csv
from src.model import train_linear_model
from src.tracking import build_tracker


def compute_metrics(targets: list[float], predictions: list[float]) -> dict[str, float]:
    if not targets:
        raise ValueError("Targets cannot be empty.")
    errors = [target - pred for target, pred in zip(targets, predictions)]
    mae = sum(abs(err) for err in errors) / len(errors)
    mse = sum(err * err for err in errors) / len(errors)
    return {"mae": mae, "mse": mse}


def main() -> None:
    settings = load_settings()
    dataset_path = settings.data_dir / "sample.csv"
    model_path = settings.model_dir / "linear_model.json"

    dataset = load_csv(dataset_path)
    model = train_linear_model(dataset.features, dataset.targets)
    predictions = model.predict(dataset.features)
    metrics = compute_metrics(dataset.targets, predictions)

    settings.model_dir.mkdir(parents=True, exist_ok=True)
    model.save(model_path)

    tracker = build_tracker(
        tracking_uri=settings.mlflow_tracking_uri,
        experiment_name=settings.mlflow_experiment_name,
        run_name=settings.mlflow_run_name,
    )
    tracker.log_params(
        {
            "model_type": "linear_model",
            "rows": len(dataset.targets),
            "features": len(dataset.features[0]) if dataset.features else 0,
        }
    )
    tracker.log_metrics(metrics)
    tracker.log_artifact(model_path)
    tracker.close()

    print(f"Saved model to {model_path}")
    print(f"Training metrics: MAE={metrics['mae']:.4f}, MSE={metrics['mse']:.4f}")


if __name__ == "__main__":
    main()
