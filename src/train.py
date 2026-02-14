from __future__ import annotations

from pathlib import Path

from src.config import load_settings
from src.data import load_csv
from src.model import train_linear_model


def main() -> None:
    settings = load_settings()
    dataset_path = settings.data_dir / "sample.csv"
    model_path = settings.model_dir / "linear_model.json"

    dataset = load_csv(dataset_path)
    model = train_linear_model(dataset.features, dataset.targets)

    settings.model_dir.mkdir(parents=True, exist_ok=True)
    model.save(model_path)
    print(f"Saved model to {model_path}")


if __name__ == "__main__":
    main()
