from src.train import compute_metrics


def test_compute_metrics_returns_expected_values() -> None:
    targets = [2.0, 4.0, 6.0]
    predictions = [1.0, 5.0, 5.0]
    metrics = compute_metrics(targets, predictions)
    assert metrics["mae"] == 1.0
    assert metrics["mse"] == 1.0
