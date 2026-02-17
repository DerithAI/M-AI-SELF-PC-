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
tests/          Automated tests
```

## Quickstart
1. Copy `.env.example` to `.env`.
2. Create and activate virtualenv.
3. Install package with dev dependencies:
   ```bash
   pip install -e .[dev,ml]
   ```
4. Train baseline model:
   ```bash
   python -m src.train
   ```
5. Run API:
   ```bash
   uvicorn src.serve.app:app --reload
   ```
6. Execute tests:
   ```bash
   pytest
   ```

## Next step
See `docs/next-steps.md` for a practical roadmap (2 weeks, 6 weeks, 3 months).

## Zarządzanie zadaniami
- Backlog wykonawczy: `TASKS.md`
- Roadmapa etapów: `docs/next-steps.md`


## MLflow tracking
- Training automatycznie loguje parametry, metryki i artefakt modelu przez MLflow (jeśli extra `ml` jest zainstalowany).
- Gdy MLflow nie jest dostępny, trening działa dalej z fallbackiem (Noop tracker).


## Agent bootstrap
- Szybki start agenta: `./scripts/setup_agent.sh`
- Instrukcja auto-update klienta: `docs/agent-setup.md`
```

## Quickstart (suggested)
1. Copy `.env.example` to `.env`.
2. Create a virtualenv and install dependencies.
3. Run a baseline training job: `python -m src.train`.
4. Serve the model: `uvicorn src.serve.app:app --reload`.
5. Start with `docs/architecture.md` and `docs/plan.md`.
