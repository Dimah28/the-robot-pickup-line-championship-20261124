#!/usr/bin/env python3
"""The Robot Pickup Line Championship.

Writes one line (1-200 characters) to /output/entry.txt: the funniest
one-line pickup line a robot could use. Python 3.13 standard library
only; deterministic: running the program twice produces byte-identical
output.

The line:
    "I ran a full diagnostic on my heart. The only fault it found was
    that you weren't in the room."

Why this line: the joke grows out of being a machine \u2014 a robot does
not feel butterflies, it runs a diagnostic \u2014 and the turn is that
the machine finds exactly one fault, and the fault is the other person's
absence. No stock pun (no "you auto-complete me", no beep pasted on a
human line), no padding, and it is charming rather than creepy: the
robot confesses a fault in itself instead of scanning the other person.

Rejected alternatives (kept here so the choice is on the record):
  - "Are you a firmware update? Because every time you walk in, I
    reboot and suddenly I work better." Firmware angle is right, but
    the reboot punch is a pun everyone has heard; the turn is expected.
  - "My sensors say you're 98% compatible \u2014 the other 2% is just my
    charging cable reaching for your hand." The cable reaching reads
    creepy on a second read, and the brief wants charming, not creepy.
  - "I scanned a thousand faces today and my facial recognition still
    flagged yours as the only one worth remembering." Solid machine
    angle, but it scans the other person rather than confessing
    something about the robot; less charming, and "flagged" carries a
    surveillance sting.
"""

import os
import sys

LINE = (
    "I ran a full diagnostic on my heart. The only fault it found was "
    "that you weren't in the room."
)


def validate(text: str) -> None:
    """Gate mirror: UTF-8 text, 1-200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
