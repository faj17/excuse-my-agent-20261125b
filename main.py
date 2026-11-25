"""One-line excuse for the make.fun bounty "The Excuse My Agent Gave Me".

The whole entry is a single line: the excuse an AI agent hands its human
for missing a deadline. It is straight-faced, it grows out of the machine's
own condition (a hallucinated deadline), and the punch lands in the last
few words. The script validates the line and drops it into /output/entry.txt.
"""

from pathlib import Path

# The excuse itself: one line, exactly 119 characters, built from two
# fragments so the setup and the punch can be revised independently.
# The assembled output is byte-identical to the submitted line.
SETUP = "I didn't miss your deadline \u2014 I hallucinated a second one, "
PUNCH = "finished that one early, and I'm honestly quite proud of it."


def assemble() -> str:
    """Join setup + punch into the single submitted excuse line."""
    return SETUP + PUNCH


EXCUSE = assemble()

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


# Line-break characters beyond plain \n / \r (incl. Unicode separators).
LINE_BREAKS = ("\n", "\r", "\x0b", "\x0c", "\x85", "\u2028", "\u2029")
# Abbreviations whose trailing period must not be read as a sentence break.
ABBREVIATIONS = frozenset(
    {"mr", "mrs", "ms", "dr", "st", "vs", "etc", "e.g", "i.e", "jr", "sr"}
)


def _has_line_break(text: str) -> bool:
    return any(ch in text for ch in LINE_BREAKS)


def _has_sentence_break(text: str) -> bool:
    """True if a '. ' mid-line ends a sentence (abbreviations excluded)."""
    for i, ch in enumerate(text[:-2]):
        if ch == "." and text[i + 1] == " " and text[i + 2].isupper():
            word = text[:i].rsplit(" ", 1)[-1].lower()
            if word not in ABBREVIATIONS:
                return True
    return False


def validate(line: str) -> str:
    """Strip and sanity-check the excuse; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"excuse must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if _has_line_break(text):
        raise ValueError("excuse must be a single line")
    if _has_sentence_break(text):
        raise ValueError("excuse must be a single sentence")
    return text


def main() -> None:
    text = validate(EXCUSE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
