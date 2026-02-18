from pathlib import Path

import pytest

from src.data import load_csv
from src.model import LinearModel, train_linear_model


def test_load_csv_reads_sample() -> None:
    dataset = load_csv(Path("data/sample.csv"))
    assert len(dataset.features) == 5
    assert len(dataset.targets) == 5


def test_train_and_save_model(tmp_path: Path) -> None:
    dataset = load_csv(Path("data/sample.csv"))
    model = train_linear_model(dataset.features, dataset.targets, epochs=300)

    preds = model.predict(dataset.features)
    mae = sum(abs(t - p) for t, p in zip(dataset.targets, preds)) / len(dataset.targets)
    assert mae < 0.2

    out = tmp_path / "model.json"
    model.save(out)
    loaded = LinearModel.load(out)
    assert loaded.predict([[1.0, 2.0]]) == model.predict([[1.0, 2.0]])


def test_predict_row_rejects_wrong_feature_count() -> None:
    model = LinearModel(weights=[1.0, 2.0], bias=0.5)

    with pytest.raises(ValueError, match="Expected 2 features, received 1"):
        model.predict_row([1.0])
