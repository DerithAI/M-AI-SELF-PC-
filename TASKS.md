# TASKS (Execution Backlog)

## Sprint 0 — Stabilizacja baseline
- [ ] Dodać walidację wejścia CSV (brakujące kolumny, typy, puste rekordy) w `src/data.py`.
- [x] Dodać metryki treningowe (MAE, MSE) i logowanie wyniku w `src/train.py`.
- [ ] Dodać endpoint `/version` w `src/serve/app.py`.
- [ ] Dodać testy regresyjne dla błędnych payloadów `/predict`.

## Sprint 1 — Reproducibility & MLOps
- [x] Integracja MLflow w treningu (params, metrics, artifacts).
- [ ] Rejestrowanie modelu po treningu (nazwa + wersja).
- [ ] Pipeline CI: lint + test + build.
- [ ] Przygotować Dockerfile dla serwisu inferencji.

## Sprint 2 — Production Readiness
- [ ] Monitoring inferencji (latency, throughput, error rate).
- [ ] Drift detection dla cech wejściowych.
- [ ] Canary rollout dla nowych modeli.
- [ ] Procedura rollback i runbook incydentów.
