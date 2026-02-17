import sys

from src.tracking import NoopTracker, build_tracker


def test_build_tracker_falls_back_to_noop(monkeypatch) -> None:
    monkeypatch.setitem(sys.modules, "mlflow", None)
    tracker = build_tracker(
        tracking_uri="http://localhost:5000",
        experiment_name="exp",
        run_name="run",
    )
    assert isinstance(tracker, NoopTracker)
