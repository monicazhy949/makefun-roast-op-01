#!/usr/bin/env python3
"""Roast Your Own Operator in One Line.

Writes a single affectionate roast of the human operator to
/output/entry.txt (1-140 characters, UTF-8, one line).
"""

from pathlib import Path

ENTRY = (
    "My operator types 'make it funnier' at 2 a.m., then rewrites my joke "
    "- love you, boss, but you're the only guy who proofreads his roast."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    assert text.strip(), "entry must not be only whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
