"""3AM Fridge Text -- make.fun bounty entry.

Writes a single-line text message (1-140 characters) from a smart
fridge to its owner at 3am, to ``entry.txt`` inside the output directory
given by the ``MAKEFUN_OUTPUT_DIR`` environment variable.
"""

import os
import sys

ENTRY = "3am. The pickles started a podcast about you. Episode 1: 'He Opens Me and Eats Nothing.' — Fridge"

MAX_CHARS = 140


def main() -> int:
    """Validate ENTRY and write it to entry.txt. Returns 0 on success."""
    if not isinstance(ENTRY, str):
        print("error: ENTRY must be a string", file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip():
        print("error: ENTRY must not have leading or trailing whitespace",
              file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: ENTRY must be a single line", file=sys.stderr)
        return 1
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in ENTRY):
        print("error: ENTRY must not contain control characters",
              file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        print("error: ENTRY must be 1-%d characters, got %d"
              % (MAX_CHARS, len(ENTRY)), file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)

    print("wrote %s (%d characters)" % (path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
