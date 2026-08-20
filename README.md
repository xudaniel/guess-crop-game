# Guess the Crop

[![local-only](https://img.shields.io/badge/network-127.0.0.1_only-blue)](#privacy)
[![python](https://img.shields.io/badge/python-3.9%2B-blue)](#requirements)
[![deps](https://img.shields.io/badge/dependencies-none_(stdlib)-success)](#requirements)
[![sfw](https://img.shields.io/badge/content-SFW-brightgreen)](#content-policy)
[![license](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)
[![CI](https://github.com/xudaniel/guess-crop-game/actions/workflows/ci.yml/badge.svg)](https://github.com/xudaniel/guess-crop-game/actions/workflows/ci.yml)

> **Photo crop quiz** for a local image library.  
> See a cropped region → pick which full photo it came from (4 choices).

Runs entirely on your machine. Images are never uploaded.

---

## Preview

```text
┌──────────────────────┬─────────────────────────┐
│   [ tight crop ]     │  Which photo is this?   │
│   canvas crop        │  ┌─────┐  ┌─────┐       │
│                      │  │ 1   │  │ 2   │       │
│   timer ▓▓▓▓░░░░     │  └─────┘  └─────┘       │
│                      │  ┌─────┐  ┌─────┐       │
│                      │  │ 3   │  │ 4   │       │
│                      │  └─────┘  └─────┘       │
└──────────────────────┴─────────────────────────┘
```

---

## Quick start

```bash
cd path/to/guess-crop-game
./scripts/start.sh
```

Open **http://127.0.0.1:8765/**

Or open the browser for you:

```bash
./scripts/dev.sh
```

Stop with `Ctrl+C`.

### One-liner

```bash
python3 app/server.py
```

### Point at your photo library

By default the server uses the **parent directory** of this repo as the library root (sibling folders become selectable packs).

```bash
export GUESS_CROP_LIBRARY="$HOME/Pictures/MyAlbumPacks"
./scripts/start.sh
```

Example library layout:

```text
MyAlbumPacks/                 ← GUESS_CROP_LIBRARY
├── landscapes/
├── pets/
├── family-vacation/
└── guess-crop-game/          ← this repo (ignored as a pack)
```

---

## Features

- **4 crop modes** — face/top, mid-frame, detail, chaos
- **4 difficulty levels** — easy → extreme (tiny crops)
- **Same-folder distractors** — harder lookalikes from one pack
- **Rush mode** — optional timer, lives, speed bonus
- **Folder picker** — choose which packs to load
- **Score + streak** — best streak saved in the browser
- **Keyboard** — `1`–`4` choose, `N`/`Space` next, `S` skip
- **Local-only server** — binds to localhost by default

Feature stories: **[docs/stories.md](docs/stories.md)**

---

## Content policy

This project is **SFW (safe for work)** and **nonsexual** by design:

- Copy, docs, and UI refer to ordinary **photos**, not adult content
- No NSFW assets are included in the repository
- You supply your own local image folders
- Please do not publish or commit unlawful or non-consensual imagery

Use family photos, travel albums, pets, product shots, art studies, etc.

---

## Repository layout

```text
guess-crop-game/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── .gitignore
├── .github/
│   └── ISSUE_TEMPLATE.md
├── app/
│   └── server.py             ← HTTP API + static host
├── web/
│   └── index.html            ← game UI (HTML/CSS/JS)
├── scripts/
│   ├── start.sh
│   └── dev.sh
└── docs/
    ├── gameplay.md
    ├── architecture.md
    ├── configuration.md
    └── stories.md
```

---

## Requirements

| Thing | Notes |
|-------|--------|
| macOS / Linux / Windows* | *use Python 3; shell scripts are bash |
| Python **3.9+** | **No pip packages** — stdlib only |
| Browser | Chrome, Safari, Firefox, Edge |

---

## Play

1. Start the server
2. Select photo folders
3. Pick **mode**, **difficulty**, optional **rush**
4. **Start game**
5. Match the crop to the correct full image

More detail: **[docs/gameplay.md](docs/gameplay.md)**

---

## API (local)

| Endpoint | Description |
|----------|-------------|
| `GET /` | Game UI |
| `GET /api/health` | Paths + ok status |
| `GET /api/folders` | Available library folders |
| `GET /api/images?folders=A,B&limit=300` | Image deck metadata |
| `GET /img/<relative-path>` | Image bytes from library |

See **[docs/architecture.md](docs/architecture.md)**.

---

## Configuration

```bash
GUESS_CROP_LIBRARY="$HOME/Pictures/Albums" GUESS_CROP_PORT=9000 ./scripts/start.sh
```

| Env var | Default | Meaning |
|---------|---------|---------|
| `GUESS_CROP_LIBRARY` | parent of this repo | Image library root |
| `GUESS_CROP_HOST` | `127.0.0.1` | Bind address |
| `GUESS_CROP_PORT` | `8765` | Port |

Full notes: **[docs/configuration.md](docs/configuration.md)**

---

## Privacy

- Server listens on **localhost only** by default
- No analytics, no accounts, no uploads
- Your photos stay on disk under the library root
- Do **not** commit personal photo libraries into this repo

---

## Contributing

See **[CONTRIBUTING.md](CONTRIBUTING.md)**.

---

## License

[MIT](LICENSE) — code only. Your photos remain yours.

---

## Roadmap

- [x] Same-folder distractors
- [x] Rush mode (timer + lives + speed bonus)
- [ ] Post-round reveal polish (crop overlay on full photo)
- [ ] Session review of missed rounds
- [ ] Optional sound cues
- [ ] Additional mini-games in a monorepo later
