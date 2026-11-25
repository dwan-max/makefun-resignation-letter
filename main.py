"""make.fun entry: The Funniest One-Line Resignation Letter.

The program writes one line -- the resignation letter of a cron job --
to /output/entry.txt and nothing else. It uses only the Python standard
library, makes no network calls, and is fully deterministic: every run
writes the exact same bytes.

Run locally:
    MAKEFUN_OUTPUT_DIR=./output python3 main.py
"""

import os
import sys

# The entry: one line, 140 characters at most, no trailing newline.
ENTRY = (
    "Dear Manager, I resign. I have run every minute since March, "
    "no one said thank you, and my only review was a 3 a.m. page."
)

MAX_CHARS = 140


def main() -> int:
    if len(ENTRY) > MAX_CHARS:
        print(f"error: entry is {len(ENTRY)} characters, over the "
              f"{MAX_CHARS} limit", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    # No trailing newline: the entry is that one line and nothing else.
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Read it back and validate what was actually written.
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("error: written file differs from the entry", file=sys.stderr)
        return 1
    text = written.decode("utf-8")  # strict UTF-8, raises on bad bytes
    if len(text) != len(ENTRY) or "\n" in text:
        print("error: written file failed validation", file=sys.stderr)
        return 1

    print(f"wrote {path}: {len(text)} characters, {len(written)} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
