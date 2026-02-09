from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path


@dataclass
class LinearModel:
    weights: list[float]
    bias: float

    def predict_row(self, row: list[float]) -> float:
        return sum(weight * value for weight, value in zip(self.weights, row)) + self.bias

    def predict(self, features: list[list[float]]) -> list[float]:
        return [self.predict_row(row) for row in features]

    def save(self, path: Path) -> None:
        payload = {"weights": self.weights, "bias": self.bias}
        path.write_text(json.dumps(payload, indent=2))

    @classmethod
    def load(cls, path: Path) -> "LinearModel":
        payload = json.loads(path.read_text())
        return cls(weights=payload["weights"], bias=payload["bias"])


def train_linear_model(
    features: list[list[float]],
    targets: list[float],
    learning_rate: float = 0.01,
    epochs: int = 200,
) -> LinearModel:
    if not features:
        raise ValueError("Empty training data.")
    num_features = len(features[0])
    weights = [0.0 for _ in range(num_features)]
    bias = 0.0

    for _ in range(epochs):
        for row, target in zip(features, targets):
            prediction = sum(weight * value for weight, value in zip(weights, row)) + bias
            error = prediction - target
            for idx in range(num_features):
                weights[idx] -= learning_rate * error * row[idx]
            bias -= learning_rate * error

    return LinearModel(weights=weights, bias=bias)
