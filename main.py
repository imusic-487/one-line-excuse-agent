#!/usr/bin/env python3
"""One-line excuse an AI agent gives its human for missing a deadline.

Reads the entry line from line.txt (shipped in this repo), validates it
against the gate (UTF-8 text, 1-160 characters, not only whitespace),
and writes it byte for byte to /output/entry.txt.
Standard library only; no network, no secrets, no input besides line.txt.
"""

import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "line.txt"
DEST = Path("/output/entry.txt")
MAX_CHARS = 160


def main() -> int:
    try:
        text = SOURCE.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"error: cannot read {SOURCE}: {exc}", file=sys.stderr)
        return 1

    if not 1 <= len(text) <= MAX_CHARS:
        print(
            f"error: entry is {len(text)} characters, "
            f"must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("error: entry is only whitespace", file=sys.stderr)
        return 1

    try:
        DEST.parent.mkdir(parents=True, exist_ok=True)
        DEST.write_bytes(text.encode("utf-8"))
    except OSError as exc:
        print(f"error: cannot write {DEST}: {exc}", file=sys.stderr)
        return 1

    print(
        f"wrote {DEST}: {len(text)} characters, "
        f"{len(text.encode('utf-8'))} bytes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
