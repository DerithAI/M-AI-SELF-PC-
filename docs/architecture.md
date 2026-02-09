# Architecture (ML-first)

## Overview
This project follows an ML-first architecture that prioritizes experimentation speed,
reproducibility, and reliable deployment.

## Core Components
1. **Data Layer**
   - Storage: S3/GCS/local for datasets and artifacts.
   - Data validation: Great Expectations.
   - Feature store: Feast (optional, when features are reused across models).

2. **Experimentation & Training**
   - Framework: PyTorch.
   - Experiment tracking: MLflow or Weights & Biases.
   - Hyperparameter tuning: Optuna.

3. **Model Registry & Artifacts**
   - Registry: MLflow Model Registry.
   - Artifacts: saved in `models/` and object storage.

4. **Serving**
   - API: FastAPI.
   - Inference: TorchServe or Triton for production.
   - Cache: Redis for hot paths.

5. **MLOps**
   - Pipelines: GitHub Actions + DVC.
   - Monitoring: Evidently AI for data drift, Prometheus/Grafana for infra.

## Data Flow (High-Level)
1. Raw data is ingested and validated.
2. Features are created and versioned.
3. Training jobs run with experiment tracking.
4. Best models are registered and deployed.
5. Inference is monitored for drift and performance.

## Interfaces
- **Training pipeline**: CLI scripts in `scripts/`.
- **Serving API**: `src/serve/`.
- **Batch jobs**: `src/batch/` or scheduled pipeline.

## Non-Functional Requirements
- Reproducibility through versioned data + code.
- Scalability via containerized workloads.
- Observability at data, model, and service layers.
