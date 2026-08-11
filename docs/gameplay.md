# Gameplay

## Goal

Match a **cropped region** of a photo to the correct full image among **four** choices.

## Modes

| Mode | Crop region | Prompt |
|------|-------------|--------|
| **Face / top** | Upper portion of the image | Which full photo is this? |
| **Mid-frame** | Middle / lower band | Which full image is this crop from? |
| **Detail** | Tight random crop | Which full image owns this detail? |
| **Chaos** | Random mix of the above | Surprise |

## Difficulty

| Level | Crop size (approx.) |
|-------|---------------------|
| Easy | ~42% of image edge |
| Normal | ~28% |
| Hard | ~18% |
| Extreme | ~11% (very small crop) |

## Same-folder distractors

Toggle in setup (default **ON**).

- When ON, the 3 wrong options prefer the **same pack** as the correct image.
- Nested packs (`library/pack/subfolder/...`) use a two-level key when helpful.
- If a pack is too thin in the deck, the game fills from other folders and notes `mixed (thin folder)`.

## Rush mode

Optional timer under the crop:

| Setting | Meaning |
|---------|---------|
| Off | No timer |
| Rush 3.0s / 2.0s / Panic 1.5s | Answer before the bar empties |

- **Lives** (3 / 5 / 1 / ∞): wrong, timeout, or skip costs a life when finite.
- **0 lives** → game over (return via Settings).
- **Speed bonus** (optional): faster answers score extra points.

## Scoring

- Correct answer: base **1 + floor(streak / 3)**, plus optional speed bonus
- Wrong, timeout, or skip (before answer): streak → **0**, lose a life if finite
- **Best streak** is stored in browser `localStorage` (`gtc_best`)

## Controls

| Input | Action |
|-------|--------|
| Click option | Choose |
| `1` `2` `3` `4` | Choose option |
| `N` / `Space` | Next round (after answer) |
| `S` | Skip / reveal answer |

## Tips

- Prefer folders with varied subjects for harder rounds.
- Same-folder decks make distractors more similar.
- Raise **pool size** for less repetition on large libraries.

## Stories

Product stories: **[stories.md](stories.md)**
