#!/usr/bin/env bash
# Dev helper: start server and open browser
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PORT="${GUESS_CROP_PORT:-8765}"
URL="http://127.0.0.1:${PORT}/"

# open browser shortly after server would bind
(sleep 0.6 && open "$URL") &

exec "$ROOT/scripts/start.sh"
