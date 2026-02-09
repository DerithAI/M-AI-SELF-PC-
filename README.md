# M-AI-SELF-PC-

ML-first scaffold for rapid experimentation, training, and deployment.

## Goals
- Fast iteration on models with reproducible experiments.
- Clear separation of data, training, serving, and ops.
- Infrastructure-ready structure for productionization.

## Structure
```
docs/           Architecture and planning docs
data/           Data contracts, schemas, samples
models/         Model artifacts and checkpoints (gitignored)
notebooks/      Exploratory notebooks
scripts/        Utility scripts for data and training
src/            Application and ML code
infra/          Deployment, CI/CD, and infra configs
```

## Quickstart (suggested)
1. Copy `.env.example` to `.env`.
2. Create a virtualenv and install dependencies.
3. Run a baseline training job: `python -m src.train`.
4. Serve the model: `uvicorn src.serve.app:app --reload`.
5. Start with `docs/architecture.md` and `docs/plan.md`.
