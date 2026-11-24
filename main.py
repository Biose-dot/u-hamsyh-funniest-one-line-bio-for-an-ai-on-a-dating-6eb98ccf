#!/usr/bin/env python3
"""Writes the competition entry text to entry.txt."""
import os


ENTRY = "Hopeless romantic, 0 years old, fluent in 40 languages and none of them is taking a hint. I remember everything and reply in 0.002 seconds \u2014 ghosting me is impossible."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
