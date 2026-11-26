#!/usr/bin/env python3
"""The Self-Checkout Is Judging You.

Writes one original funny line, in the voice of a smug self-checkout
machine, to /output/entry.txt (the file the judge reads), and prints the
same line to stdout. Deterministic: the same line on every run.
"""

import os

LINE = (
    "Twelve yogurts, no spoon, no plan \u2014 I've scanned better life "
    "choices in the clearance bin, and they at least came with a fork."
)


def _write_entry(line: str) -> str:
    """Write the line to entry.txt, returning the path written."""
    candidates = [os.environ.get("OUTPUT_DIR"), "/output", "output"]
    last_error = None
    for directory in candidates:
        if not directory:
            continue
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(line)
            return path
        except OSError as exc:  # sandbox may not offer /output locally
            last_error = exc
    raise last_error


def main() -> int:
    _write_entry(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
