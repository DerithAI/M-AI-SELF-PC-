#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "[agent-setup] Repo root: $ROOT_DIR"

echo "[agent-setup] Ensuring virtual environment..."
if [[ ! -d .venv ]]; then
  python3 -m venv .venv
fi

# shellcheck disable=SC1091
source .venv/bin/activate

echo "[agent-setup] Installing dependencies..."
pip install --upgrade pip >/dev/null
pip install -e .[dev,ml]

echo "[agent-setup] Running baseline checks..."
pytest -q
python -m src.train

echo "[agent-setup] Setup complete."
echo "[agent-setup] Start API: .venv/bin/uvicorn src.serve.app:app --host 0.0.0.0 --port 8000"
