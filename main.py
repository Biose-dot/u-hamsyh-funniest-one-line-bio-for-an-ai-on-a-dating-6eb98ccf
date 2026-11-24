#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App — make.fun entry.

Writes the entry text (no trailing newline, nothing else) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Reads as a dating bio, sounds like a character, and lands the laugh in the last clause: the AI's inhuman traits turned into dating virtues, ending on the one thing it cannot do.
"""
import os

ENTRY = 'AI, age 0, emotionally available 24/7. I never sleep, I never forget what you said, and I reply in 0.002 seconds. Swipe right — I literally cannot ghost you.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
