#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOCK_FILE="/tmp/m-ai-self-pc-update.lock"
cd "$ROOT_DIR"

exec 9>"$LOCK_FILE"
flock -n 9 || {
  echo "[client-update] Another update is already running."
  exit 0
}

BRANCH="${UPDATE_BRANCH:-work}"
REMOTE="${UPDATE_REMOTE:-origin}"

echo "[client-update] Updating from $REMOTE/$BRANCH"
if git remote get-url "$REMOTE" >/dev/null 2>&1; then
  git fetch "$REMOTE" "$BRANCH"
  git checkout "$BRANCH"
  git pull --ff-only "$REMOTE" "$BRANCH"
else
  echo "[client-update] Remote '$REMOTE' not configured, skipping git pull."
fi

if [[ ! -d .venv ]]; then
  python3 -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate

pip install -e .[dev,ml]
pytest -q
python -m src.train

echo "[client-update] Update complete."
