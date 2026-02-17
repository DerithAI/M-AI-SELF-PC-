# Co dalej? (Roadmap wykonawczy)

## Aktualny status
- ✅ Bazowy pipeline treningu działa (`python -m src.train`).
- ✅ API inferencyjne działa (`/health`, `/predict`).
- ✅ Testy jednostkowe i API są dostępne (`pytest`).
- 🔜 Kolejny krok: obserwowalność, jakość danych i automatyzacja MLOps.

## Najbliższe 2 dni
1. Ustalić metrykę główną (np. MAE/F1) i akceptowalne progi jakości.
2. Podłączyć realne źródło danych (zamiast `data/sample.csv`).
3. Dodać walidację danych wejściowych (schema checks).
4. Dodać checklistę release'u modelu (pre/post deploy).

## Najbliższe 2 tygodnie
1. Dodać eksperyment tracking (MLflow/W&B) do `src/train.py`.
2. Rozszerzyć model o pipeline feature engineering.
3. Dodać endpoint `/version` i metryki inferencji.
4. Dodać testy integracyjne dla całego flow train -> serve.

## Najbliższe 6 tygodni
1. Zbudować automatyczny pipeline CI/CD (testy + build obrazu).
2. Uruchomić środowisko staging (Docker Compose/Kubernetes).
3. Dodać monitoring driftu danych i jakości predykcji.
4. Wdrożyć bezpieczny rollout modelu (canary / rollback).

## Najbliższe 3 miesiące
1. Feature Store i standaryzacja cech między treningiem a inferencją.
2. Automatyczny retraining oparty o drift i KPI biznesowe.
3. Dashboard SLA/SLO (latency, error rate, model quality).
4. Hardening bezpieczeństwa (sekrety, IAM, audyt).
