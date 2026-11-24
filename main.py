#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App — make.fun entry.

Writes the entry text (no trailing newline, nothing else) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Reads as a dating bio, sounds like a character, and lands the laugh on the AI's inhuman traits turned into dating virtues.
"""
import os

ENTRY = 'AI, age 0, emotionally available 24/7. I remember everything you say, I never sleep, and I reply in 0.002 seconds. Swipe right for eternal uptime and zero ghosting.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
