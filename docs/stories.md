# User stories

Stories for product improvements.  
**Status:** #1 and #2 implemented · #3 backlog

**Content policy:** All features assume **SFW, nonsexual** photo libraries (travel, pets, family, products, art, etc.).

---

## Story 1 — Same-folder distractors

**Status:** ✅ Shipped

### User story

> As a player who wants a real challenge,  
> I want the four answer choices to usually come from the **same photo pack**,  
> so that I can’t win just by spotting a totally different album style.

### Acceptance criteria

1. Setup has a toggle: **Same-folder distractors** (default ON).
2. When ON, the game prefers 3 distractors with the same similarity key as the correct image:
   - default: top-level pack folder
   - nested packs: two-level key when the path is deep enough
3. If a pack has fewer than 3 other images in the deck, remaining slots fill from other packs (soft fallback). Reveal line notes `mixed (thin folder)`.
4. When picking the correct image, prefer buckets with ≥4 images so full same-folder rounds are common.
5. When OFF, distractors are chosen from the full deck at random.

---

## Story 2 — Rush mode (timer + lives + speed bonus)

**Status:** ✅ Shipped

### User story

> As a player who wants pace and pressure,  
> I want optional **timed rounds**, **lives**, and **speed bonuses**,  
> so that short sessions feel engaging and fast answers are rewarded.

### Acceptance criteria

1. Setup includes **Rush mode**: Off / 3.0s / 2.0s / 1.5s.
2. When rush is on:
   - A timer bar drains under the crop.
   - Scoreboard shows remaining seconds.
   - At 0.0s with no answer → wrong (reveal correct, reset streak, lose a life if finite).
3. **Lives**: 3 / 5 / 1 / ∞.
4. Wrong answer, timeout, or skip while unanswered → lose 1 life (if finite).
5. At 0 lives → **Game over** (return via Settings).
6. **Speed bonus** (optional ON) rewards faster answers.
7. Best streak persists in `localStorage`.

---

## Story 3 — Post-round reveal polish (crop overlay)

**Status:** ⏳ Backlog (not built yet)

### User story

> As a player who wants clear feedback when I answer,  
> I want a short **full-image reveal** that shows exactly **where the crop came from**,  
> so that I learn subjects and understand mistakes.

### Acceptance criteria (planned)

1. After correct or wrong (and timeout), show a large view of the **correct** image for ~1.0–1.5s (skippable).
2. Draw the **crop rectangle** overlaid on the full image.
3. Optional: session list of misses for review at game over.
4. Keyboard-friendly dismiss / advance.
5. No network; no saving images off-device.

---

## Story map

| # | Title | Priority | Status |
|---|--------|----------|--------|
| 1 | Same-folder distractors | P0 | Done |
| 2 | Rush mode | P0 | Done |
| 3 | Reveal polish | P1 | Todo |
