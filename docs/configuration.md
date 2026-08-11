# Configuration

## Environment variables

| Variable | Default | Description |
|----------|---------|-------------|
| `GUESS_CROP_LIBRARY` | parent of this repo | Root folder containing photo packs |
| `GUESS_CROP_HOST` | `127.0.0.1` | Bind address |
| `GUESS_CROP_PORT` | `8765` | HTTP port |

Example:

```bash
export GUESS_CROP_LIBRARY="$HOME/Pictures/Albums"
GUESS_CROP_PORT=9000 ./scripts/start.sh
```

## Image library root

```text
Albums/                       ← GUESS_CROP_LIBRARY
├── landscapes/
├── pets/
├── product-shots/
└── guess-crop-game/          ← this repo (auto-skipped as a pack)
```

Packs are **top-level subdirectories** of the library root. The game repo name is ignored so it can live next to your albums.

## Runtime requirements

- **Python 3.9+** (stdlib only — no `pip install`)
- Modern browser
