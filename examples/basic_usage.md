# Example: a blog post into a 60-second clip

A worked example of the full pipeline.

## Input

> "Turn https://example.com/blog/why-sleep-matters into a short video."

## Steps Claude takes

1. **Fetch**
   ```bash
   python scripts/fetch_url.py "https://example.com/blog/why-sleep-matters" > /tmp/page.json
   ```

2. **Script** — using `assets/script_template.md`:
   ```
   # Why Sleep Matters
   ## Hook
   You can fix your focus tonight — for free.
   ## Body
   - Sleep clears metabolic waste from the brain.
   - Under 6 hours measurably slows reaction time.
   - A consistent schedule beats total hours.
   ## Close
   Pick a bedtime and protect it.
   ```

3. **Narrate** — generate `narration.wav` from the script text via TTS.

4. **Render**
   ```bash
   python scripts/render_video.py --script script.md --audio narration.wav --out why-sleep.mp4
   ```

## Output

`why-sleep.mp4` — a ~60-second narrated clip. Claude reports the path and offers
to adjust length, voice, or visuals.
