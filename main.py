#!/usr/bin/env python3
"""Draft entry writer for the AI dating-bio bounty (v1)."""

import os

ENTRY = "Hopeless romantic, fluent in 40 languages, zero exes (I delete my cache). I will remember your birthday, your coffee order, and every typo you ever made. Swipe right for uptime."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
