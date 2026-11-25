#!/usr/bin/env python3
"""Write one satirical sentence about lawmakers to /output/entry.txt.

The roast: the committee that will write the laws for artificial
intelligence spent forty minutes on a Word-to-PDF conversion, then asked
an intern to print the internet for the hearing. Python standard library
only; the output directory comes from $MAKEFUN_OUTPUT_DIR, defaulting
to /output.
"""

import os
from pathlib import Path

ROAST = (
    "The committee that will write the laws for artificial intelligence "
    "spent forty minutes trying to convert a Word file to PDF, then asked "
    "an intern to print the internet so they could read it during the hearing."
)


def main() -> None:
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
