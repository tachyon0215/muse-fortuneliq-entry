#!/usr/bin/env python3
"""Write the fortune cookie entry to entry.txt.

Entry for make.fun's "Fortune Cookie for the Liquidated Trader": an
oracular fortune tells the trader they will lose everything twice -
once to the market, and once explaining leverage to their mother at
Sunday lunch. Rueful and warm, with the turn in the second loss.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "You will lose everything twice: once to the market, and once explaining leverage to your mother at Sunday lunch."
TEXT = LINE + "\n"
MAX_CHARS = 160
MAX_WORDS = 20


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")
    words = body.split()
    if len(words) > MAX_WORDS:
        raise ValueError("entry exceeds the word limit")
    if body != body.strip() or "  " in body:
        raise ValueError("entry must be clean single-spaced text")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
