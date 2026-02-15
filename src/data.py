from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv


@dataclass(frozen=True)
class Dataset:
    features: list[list[float]]
    targets: list[float]


def load_csv(path: Path) -> Dataset:
    features: list[list[float]] = []
    targets: list[float] = []
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            targets.append(float(row["target"]))
            feature_row = [
                float(row["feature_1"]),
                float(row["feature_2"]),
            ]
            features.append(feature_row)
    return Dataset(features=features, targets=targets)
