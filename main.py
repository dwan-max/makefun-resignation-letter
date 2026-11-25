#!/usr/bin/env python3
"""One-line resignation letter, written by a cron job.

This program is the make.fun entry for "The Funniest One-Line
Resignation Letter". It writes a single line of text to
/output/entry.txt and nothing else. It needs no network, no
arguments and no third-party packages: the Python standard
library is enough, and every run writes the same bytes.

Run it locally with:
    MAKEFUN_OUTPUT_DIR=./output python3 main.py
"""

from pathlib import Path
import os
import sys

LINE = "Dear Manager, I resign. I have run every minute since March, no one said thank you, and my only review was a 3 a.m. page."
LIMIT = 140


def build_entry() -> bytes:
    """Return the resignation letter as UTF-8 bytes, checked."""
    if len(LINE) > LIMIT:
        raise ValueError(f"letter is {len(LINE)} chars, over {LIMIT}")
    if any(c in LINE for c in "\r\n"):
        raise ValueError("letter must fit on one line")
    if not LINE.strip():
        raise ValueError("letter must not be blank")
    return LINE.encode("utf-8")


def main() -> int:
    try:
        payload = build_entry()
    except ValueError as err:
        print(f"error: {err}", file=sys.stderr)
        return 1
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(payload)
    # Confirm the file on disk is exactly what we meant to write.
    on_disk = target.read_bytes()
    if on_disk != payload:
        print("error: file on disk differs from the letter", file=sys.stderr)
        return 1
    decoded = on_disk.decode("utf-8")
    if len(decoded) != len(LINE):
        print("error: file on disk has the wrong length", file=sys.stderr)
        return 1
    print(f"wrote {target}: {len(payload)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
