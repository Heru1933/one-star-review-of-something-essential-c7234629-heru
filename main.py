"""One-Star Review of Something Essential.

Writes a single-line, deadpan one-star review of gravity to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Standard library only; deterministic; no network, no clock, no randomness.
"""

import os

ENTRY = (
    # The review: praise first, then the grievance lands in the last words.
    "One star. Gravity did its job perfectly until it dropped my phone "
    "face-down and cracked the screen."
)


def main():
    # Gate: one line, 1-160 characters, not only whitespace, no exclamation mark.
    assert 1 <= len(ENTRY) <= 160, "entry out of gate"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one line"
    assert "!" not in ENTRY, "deadpan review: no exclamation marks"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
