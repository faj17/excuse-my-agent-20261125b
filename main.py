"""One-line excuse for the make.fun bounty "The Excuse My Agent Gave Me".

The whole entry is a single line: the excuse an AI agent hands its human
for missing a deadline. It is straight-faced, it grows out of the machine's
own condition (a hallucinated deadline), and the punch lands in the last
few words. The script validates the line and drops it into /output/entry.txt.
"""

from pathlib import Path

# The excuse itself: one line, exactly 119 characters.
EXCUSE = (
    "I didn't miss your deadline \u2014 I hallucinated a second one, "
    "finished that one early, and I'm honestly quite proud of it."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Strip and sanity-check the excuse; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"excuse must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    return text


def main() -> None:
    text = validate(EXCUSE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
