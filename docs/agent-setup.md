# Agent setup (najpierw stawiamy agenta)

Ten dokument uruchamia lokalnego agenta/klienta oraz opcjonalny auto-update z repo.

## 1) Bootstrap środowiska
```bash
./scripts/setup_agent.sh
```

Skrypt:
- tworzy `.venv`,
- instaluje zależności `.[dev,ml]`,
- odpala testy,
- wykonuje trening baseline.

## 2) Start API agenta
```bash
.venv/bin/uvicorn src.serve.app:app --host 0.0.0.0 --port 8000
```

## 3) Auto-update klienta z repo (opcjonalnie)
1. Skonfiguruj remote:
```bash
git remote add origin <YOUR_REPO_URL>
```
2. Testowy update ręcznie:
```bash
./scripts/update_client.sh
```
3. Włącz timer systemd (co 5 min):
```bash
mkdir -p ~/.config/systemd/user
cp infra/systemd/m-ai-self-pc-updater.service ~/.config/systemd/user/
cp infra/systemd/m-ai-self-pc-updater.timer ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now m-ai-self-pc-updater.timer
systemctl --user list-timers | rg m-ai-self-pc
```

## 4) Rollback
Jeżeli update nie przejdzie:
```bash
git log --oneline -n 5
git reset --hard <PREVIOUS_COMMIT>
```
