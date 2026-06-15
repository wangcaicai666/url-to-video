# url-to-video skill

A complete Claude Code skill that turns a URL into a short video.

**This repository is itself the skill** — `SKILL.md` lives at the root. The
structure below is the recommended layout for any skill.

```
.
├── SKILL.md                  # Required. Entry point with YAML frontmatter.
├── README.md                 # Optional. Human-facing docs (this file).
├── reference/                # Docs loaded on demand to keep SKILL.md small.
│   ├── workflow.md
│   └── scripting.md
├── scripts/                  # Executable helpers Claude can run.
│   ├── fetch_url.py
│   └── render_video.py
├── assets/                   # Templates / files used to build the output.
│   └── script_template.md
└── examples/                 # Worked examples for reference.
    └── basic_usage.md
```

## Why this layout

- **SKILL.md stays short.** It only routes. Heavy detail lives in `reference/`
  and is read only when needed — this keeps context usage low.
- **`scripts/`** holds runnable code so Claude executes instead of re-deriving.
- **`assets/`** holds templates/boilerplate copied into outputs.
- **`examples/`** shows the intended end-to-end usage.

## Installing

Clone or copy this repository into one of:
- `.claude/skills/url-to-video/` in a project (project-scoped), or
- `~/.claude/skills/url-to-video/` (available in every project).

Claude discovers it automatically via the `name` + `description` in `SKILL.md`.
