#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry.

Writes exactly one letter to /output/entry.txt: "A" for coffee.

Why A: the judge weighs which letter's choice feels more vivid, funnier
or truer. Coffee is the punchier stance — the drink people reach for
first thing, defend out loud, and joke about needing before they can
function. "A" lands as the fuller, more alive answer: short, certain,
and standing on its own with nothing needed beside it.
"""

import os

LETTER = "A"  # A = coffee, B = tea


def main() -> None:
    if len(LETTER) != 1 or LETTER not in ("A", "B"):
        raise ValueError("entry must be exactly one letter, A or B")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
