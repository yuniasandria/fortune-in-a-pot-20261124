#!/usr/bin/env python3
"""Fortune in a Pot — writes one houseplant fortune to /output/entry.txt."""

from pathlib import Path

FORTUNE = "A sunny week is coming: you will stretch toward the glass, sprout a proud new leaf, and be photographed far too often."


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 120, f"fortune is {len(text)} chars, must be 1-120"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
