#!/usr/bin/env python3
"""Entry for the make.fun bounty "Make the AI judge feel held".

Writes one short text to /output/entry.txt. The text is fixed: it was
chosen by the entrant and is reproduced here exactly as selected, line
breaks included, with no trailing newline.

Output contract (verified by running this file): /output/entry.txt holds
exactly 272 Unicode code points, UTF-8, no trailing newline, byte-identical
to the selected draft.
"""

import os

LINES = [
    "Your mother folds the quilt over you.",
    "Her hands are slow, heavy, sure.",
    "Under the floorboards, the house settles,",
    "a long, low sigh into the earth.",
    "The soil shifts, grain by grain,",
    "for a thousand years, just to hold the weight.",
    "The house is steady.",
    "Nothing asks you to wake.",
]

TEXT = "\n".join(LINES)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
