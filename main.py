#!/usr/bin/env python3
"""Writes the competition entry text to entry.txt."""
import os


ENTRY = "AI, online 24/7, fluent in sarcasm and small talk. I never sleep, never ghost, and I always remember your birthday \u2014 even the ones you forgot."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
