# Full workflow

The end-to-end pipeline for turning a URL into a video.

## 1. Fetch

Run `scripts/fetch_url.py <url>` to download the page and extract clean,
readable text (title, headings, body). Output is JSON on stdout.

```bash
python scripts/fetch_url.py "https://example.com/article" > /tmp/page.json
```

## 2. Script

Read `reference/scripting.md`. Summarize `page.json` into a short narration
script using `assets/script_template.md` as the structure. Aim for ~150 words
per minute of video.

## 3. Narrate

Convert the script text into narration audio (TTS). Save as `narration.wav`.

## 4. Render

Run `scripts/render_video.py` with the script, narration, and any visuals to
produce the final `.mp4`.

```bash
python scripts/render_video.py --script script.md --audio narration.wav --out video.mp4
```

## 5. Review

Show the user the output path and a one-line summary. Offer to adjust length,
voice, or visuals.
