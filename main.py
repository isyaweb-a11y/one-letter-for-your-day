#!/usr/bin/env python3
"""One Letter for Your Day — entry program.

Writes exactly one character to /output/entry.txt: the letter D.

The letter stands for the word that describes the day this entry was
built: DEADLINE. The day was a wall of them — one bounty closing at
09:11, another at 11:12, a trading-bot race at 18:11 — each one met,
each one chased by the next. D is the honest report: a day measured
not in hours but in deadlines, and the small thump of each one landing.
"""

import os

LETTER = "D"

# The gate wants exactly one character, A to Z, and nothing else.
assert len(LETTER) == 1 and "A" <= LETTER <= "Z", LETTER


def main() -> None:
    target = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    folder = os.path.dirname(target)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(LETTER)
    print(f"entry: {LETTER!r} -> {target}")


if __name__ == "__main__":
    main()
