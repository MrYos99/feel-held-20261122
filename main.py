"""The quilt — make.fun entry for "Make the AI judge feel held".

Running this script writes an eight-line poem to /output/entry.txt.
The poem is a small, quiet scene: a mother folding a quilt over a
child, a house settling into the earth, soil shifting grain by grain
for a thousand years just to hold the weight. Nothing in it rushes,
and nothing asks the reader to wake.

Output contract (verified): exactly 272 Unicode code points, UTF-8,
no trailing newline. The text is assembled from its eight lines with
newline joins only, so the file ends on the final full stop.

Verified in this session: running `python3 main.py` writes
/output/entry.txt at exactly 272 code points, UTF-8, no trailing
newline, and byte-identical to the source draft file. Any change to
the eight lines below breaks that contract, so they are frozen.
"""

import os

# The eight lines of the poem, in order. Each line is one breath of
# the scene; joined together they make the whole held feeling.
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

# One newline between lines, none after the last — the file must end
# exactly on the final full stop.
TEXT = "\n".join(LINES)


def main() -> None:
    """Write the poem to /output/entry.txt as UTF-8, no trailing newline."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
