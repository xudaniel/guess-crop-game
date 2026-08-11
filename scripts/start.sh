#!/usr/bin/env bash
# Start Guess the Crop local server
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

PORT="${GUESS_CROP_PORT:-8765}"
HOST="${GUESS_CROP_HOST:-127.0.0.1}"

echo "→ Starting Guess the Crop on http://${HOST}:${PORT}/"
echo "→ Repo: $ROOT"
if [[ -n "${GUESS_CROP_LIBRARY:-}" ]]; then
  echo "→ Library: $GUESS_CROP_LIBRARY"
fi
exec python3 "$ROOT/app/server.py"
