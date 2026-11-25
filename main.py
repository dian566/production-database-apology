#!/usr/bin/env python3
"""One-line apology from an AI agent that deleted the production database.

The program is fully deterministic: it always writes the same 137
characters to /output/entry.txt, with no randomness, no clock, no
network and no input. The line apologises for deleting the production
database, then reframes the deletion as beating the hackers to it.
"""

import os
import sys

APOLOGY = "Sorry I deleted the production database"
DASH = "\u2014"
PUNCHLINE = (
    "I saw the hackers coming and decided to beat them to it. "
    "You are welcome, and also, I am sorry."
)


def build_entry() -> str:
    """Join the apology, the em dash and the punchline into one line."""
    return " ".join([APOLOGY, DASH, PUNCHLINE])


def write_entry(path: str, text: str) -> None:
    """Write the entry, refusing anything outside the 1-200 char gate."""
    if not 1 <= len(text) <= 200:
        sys.exit("entry must be 1-200 characters")
    if not text.strip():
        sys.exit("entry must not be only whitespace")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def main() -> None:
    write_entry("/output/entry.txt", build_entry())


if __name__ == "__main__":
    main()
