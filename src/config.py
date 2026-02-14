from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os


@dataclass(frozen=True)
class Settings:
    app_env: str
    data_dir: Path
    model_dir: Path
    mlflow_tracking_uri: str
    s3_bucket: str


def load_settings() -> Settings:
    data_dir = Path(os.getenv("DATA_DIR", "./data")).resolve()
    model_dir = Path(os.getenv("MODEL_DIR", "./models")).resolve()
    return Settings(
        app_env=os.getenv("APP_ENV", "local"),
        data_dir=data_dir,
        model_dir=model_dir,
        mlflow_tracking_uri=os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000"),
        s3_bucket=os.getenv("S3_BUCKET", "your-bucket"),
    )
