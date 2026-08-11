# Architecture

Local-only stack: **stdlib Python HTTP server** + **static HTML/JS** + images read from disk.

```
Browser  ──GET /──►  app/server.py  ──►  web/index.html
         ──GET /api/*──►              ──►  scan LIBRARY_ROOT folders
         ──GET /img/<relpath>──►      ──►  file bytes from LIBRARY_ROOT
```

## Paths

| Symbol | Path | Role |
|--------|------|------|
| `REPO_ROOT` | `…/guess-crop-game` | This project |
| `WEB_DIR` | `REPO_ROOT/web` | Frontend static files |
| `LIBRARY_ROOT` | env `GUESS_CROP_LIBRARY` or parent of repo | Image library |

## API

### `GET /api/health`

```json
{ "ok": true, "repo": "…", "web": "…", "library_root": "…" }
```

### `GET /api/folders`

Discovers top-level subdirectories of `LIBRARY_ROOT` (skips this repo and common junk dirs).

```json
{ "root": "/Users/…/Pictures/Albums", "folders": ["landscapes", "pets"] }
```

### `GET /api/images?folders=A,B&limit=300`

Returns a shuffled sample of images (metadata only).

```json
{
  "count": 300,
  "limit": 300,
  "folders": ["landscapes"],
  "images": [{ "id": "landscapes/…/file.jpg", "folder": "…", "name": "…" }]
}
```

### `GET /img/<relative-path>`

Serves an image file under `LIBRARY_ROOT`. Path traversal outside the library is rejected (`403`).

## Security model

- Binds to **`127.0.0.1`** by default (not LAN-exposed).
- No uploads, no cloud, no accounts.
- Image paths are constrained with `Path.resolve()` + `relative_to(LIBRARY_ROOT)`.

## Frontend

Single page: `web/index.html` (HTML + CSS + JS).

- Loads deck via `/api/images`
- Draws crops on a `<canvas>` client-side
- Never uploads images anywhere
