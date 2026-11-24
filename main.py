#!/usr/bin/env python3
"""One Letter: Coffee or Tea -- entry program.

Writes exactly one character, "A", to /output/entry.txt.
"A" stands for coffee: the bolder, more vivid answer in the
coffee-against-tea argument. Nothing else is written: no newline,
no explanation, no punctuation.

Python 3, standard library only.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
LETTER = "A"


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)

    # Self-check: the output must be exactly one character and one byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        content = f.read()
    if content != LETTER:
        raise SystemExit(f"self-check failed: entry.txt is {content!r}, expected {LETTER!r}")
    if len(content.encode("utf-8")) != 1:
        raise SystemExit("self-check failed: entry.txt is not exactly 1 byte")
    if os.path.getsize(OUTPUT_PATH) != 1:
        raise SystemExit("self-check failed: entry.txt is not exactly 1 byte on disk")
    print("OK: /output/entry.txt contains exactly one character: 'A' (coffee)")


if __name__ == "__main__":
    main()
