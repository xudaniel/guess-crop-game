#!/usr/bin/env python3
"""Local server for Guess the Crop.

Serves the web UI from ``web/`` and images from a configurable local library root.
"""

from __future__ import annotations

import json
import mimetypes
import os
import random
import urllib.parse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

# Layout:
#   guess-crop-game/          ← REPO_ROOT
#     app/server.py           ← this file
#     web/index.html
#   <library>/                ← LIBRARY_ROOT (image folders live here)
REPO_ROOT = Path(__file__).resolve().parent.parent
WEB_DIR = REPO_ROOT / "web"

# Prefer env override so the repo can live anywhere.
# Default: parent of this repo (sibling folders are photo packs).
LIBRARY_ROOT = Path(
    os.environ.get("GUESS_CROP_LIBRARY", str(REPO_ROOT.parent))
).expanduser().resolve()

# Folders under LIBRARY_ROOT to skip when auto-discovering packs
SKIP_DIR_NAMES = {
    REPO_ROOT.name.lower(),
    ".git",
    ".github",
    "node_modules",
    "__pycache__",
    ".venv",
    "venv",
}

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp"}
PORT = int(os.environ.get("GUESS_CROP_PORT", "8765"))
HOST = os.environ.get("GUESS_CROP_HOST", "127.0.0.1")


def discover_folders() -> list[str]:
    """Top-level subdirectories of LIBRARY_ROOT that look like image packs."""
    if not LIBRARY_ROOT.is_dir():
        return []
    found: list[str] = []
    for entry in sorted(LIBRARY_ROOT.iterdir(), key=lambda p: p.name.lower()):
        if not entry.is_dir():
            continue
        if entry.name.startswith("."):
            continue
        if entry.name.lower() in SKIP_DIR_NAMES:
            continue
        if entry.resolve() == REPO_ROOT.resolve():
            continue
        found.append(entry.name)
    return found


def list_images(folders: list[str], limit: int = 400) -> list[dict]:
    """Collect image paths under selected folders (relative to LIBRARY_ROOT)."""
    found: list[dict] = []
    lib = LIBRARY_ROOT.resolve()
    for folder in folders:
        root = (LIBRARY_ROOT / folder).resolve()
        if not root.is_dir():
            continue
        try:
            root.relative_to(lib)
        except ValueError:
            continue
        for dirpath, _dirnames, filenames in os.walk(root):
            for name in filenames:
                ext = Path(name).suffix.lower()
                if ext not in IMAGE_EXTS:
                    continue
                full = Path(dirpath) / name
                try:
                    rel = full.resolve().relative_to(lib)
                except ValueError:
                    continue
                found.append(
                    {
                        "id": str(rel).replace("\\", "/"),
                        "folder": folder,
                        "name": name,
                    }
                )
    random.shuffle(found)
    if limit and len(found) > limit:
        found = found[:limit]
    return found


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WEB_DIR), **kwargs)

    def log_message(self, fmt: str, *args) -> None:
        print(f"[guess-crop] {args[0]}")

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

    def do_GET(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        qs = urllib.parse.parse_qs(parsed.query)

        if path in ("/", "/index.html"):
            return self._send_file(WEB_DIR / "index.html", "text/html; charset=utf-8")

        if path == "/api/health":
            return self._json(
                {
                    "ok": True,
                    "repo": str(REPO_ROOT),
                    "web": str(WEB_DIR),
                    "library_root": str(LIBRARY_ROOT),
                }
            )

        if path == "/api/folders":
            folders = discover_folders()
            return self._json({"root": str(LIBRARY_ROOT), "folders": folders})

        if path == "/api/images":
            folders = qs.get("folders", discover_folders())
            if len(folders) == 1 and "," in folders[0]:
                folders = [x.strip() for x in folders[0].split(",") if x.strip()]
            try:
                limit = int(qs.get("limit", ["400"])[0])
            except ValueError:
                limit = 400
            limit = max(20, min(limit, 2000))
            images = list_images(folders, limit=limit)
            return self._json(
                {
                    "count": len(images),
                    "limit": limit,
                    "folders": folders,
                    "images": images,
                }
            )

        if path.startswith("/img/"):
            rel = urllib.parse.unquote(path[len("/img/") :])
            target = (LIBRARY_ROOT / rel).resolve()
            try:
                target.relative_to(LIBRARY_ROOT.resolve())
            except ValueError:
                self.send_error(403, "Forbidden")
                return
            if not target.is_file():
                self.send_error(404, "Not found")
                return
            mime, _ = mimetypes.guess_type(str(target))
            return self._send_file(target, mime or "application/octet-stream")

        return super().do_GET()

    def _json(self, obj: dict) -> None:
        data = json.dumps(obj).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _send_file(self, file_path: Path, content_type: str) -> None:
        try:
            data = file_path.read_bytes()
        except OSError:
            self.send_error(404, "Not found")
            return
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def main() -> None:
    if not (WEB_DIR / "index.html").is_file():
        raise SystemExit(f"Missing UI: {WEB_DIR / 'index.html'}")

    server = ThreadingHTTPServer((HOST, PORT), Handler)
    url = f"http://{HOST}:{PORT}/"
    print("=" * 56)
    print("  GUESS THE CROP")
    print(f"  Open:     {url}")
    print(f"  Repo:     {REPO_ROOT}")
    print(f"  Library:  {LIBRARY_ROOT}")
    print("  Stop:     Ctrl+C")
    print("=" * 56)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nBye.")
        server.server_close()


if __name__ == "__main__":
    main()
