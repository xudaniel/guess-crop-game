# Contributing

Thanks for helping improve **Guess the Crop**.

## Content policy

- This project is **SFW and nonsexual**.
- Do not add adult, explicit, or illegal content to the repo, docs, sample assets, or issue screenshots.
- Keep examples generic (pets, travel, products, nature, etc.).

## Dev loop

```bash
./scripts/dev.sh
# edit web/index.html or app/server.py
# refresh browser (responses are no-cache)
```

## Guidelines

1. Keep the server **stdlib-only** unless there is a strong reason to add dependencies.
2. Never log personal photo paths to remote services.
3. Prefer changes under `web/` for UX and `app/` for API / file access.
4. Update `docs/` when behavior or layout changes.
5. Do not commit personal image libraries into this repo.

## Suggested commits

```text
feat: add timer mode
fix: path encoding for spaces in filenames
docs: clarify library root layout
chore: ignore local scratch files
```
