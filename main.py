#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes a single sentence recalling a childhood memory to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt) and
prints it to stdout. Python 3.13 stdlib only, no network, no reads
outside this repository.
"""

import os

SENTENCE = (
    "All through third grade I kept a smooth river stone in my pocket, "
    "rubbing it during spelling tests, and thirty years later I still "
    "pat my pockets for it on bad days."
)


def main() -> None:
    # Guard the gate before writing: one clean sentence, 1-280 chars.
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 280, "sentence must be 1-280 characters"
    assert text.count(".") == 1 and text.endswith("."), "must be a single sentence"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
