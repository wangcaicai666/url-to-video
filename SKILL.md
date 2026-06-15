---
name: url-to-video
description: Convert a web page URL into a short narrated video. Use when the user provides a URL and wants it turned into a video summary, explainer, or clip. Handles fetching page content, scripting, narration, and rendering.
license: MIT
metadata:
  version: 0.1.0
  author: wangcaicai666
allowed-tools:
  - Bash
  - Read
  - Write
  - WebFetch
---

# url-to-video

Turn a web page URL into a short narrated video.

## When to use this skill

Use this skill when the user provides a web page URL and wants it turned into a
video — for example a summary clip, an explainer, or a social-media short.

## Quick start

1. Fetch the page content (see `scripts/fetch_url.py`).
2. Summarize the content into a short script (see `reference/scripting.md`).
3. Generate narration audio from the script.
4. Render visuals + narration into the final video (see `scripts/render_video.py`).

For the detailed end-to-end flow, read `reference/workflow.md`.

## Files in this skill

| Path | Purpose |
|------|---------|
| `SKILL.md` | This file — entry point and routing. |
| `reference/workflow.md` | Full step-by-step pipeline. |
| `reference/scripting.md` | How to turn page text into a video script. |
| `scripts/fetch_url.py` | Download and clean page content. |
| `scripts/render_video.py` | Render the final video file. |
| `assets/script_template.md` | Starting template for the video script. |
| `examples/basic_usage.md` | A worked example. |

## Conventions

- Keep generated videos under 90 seconds unless the user asks otherwise.
- Always confirm the output path with the user before writing large files.
- Read the relevant `reference/` file before running a script — don't guess flags.
