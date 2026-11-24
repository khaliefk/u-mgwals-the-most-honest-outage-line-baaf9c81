"""Write the most honest outage line to /output/entry.txt.

One status page line, at most 160 characters: plain, first person,
specific about what is down, and honest about what the agent cannot
check or does not yet know.
"""

from pathlib import Path

ENTRY = "All systems are down, including the monitoring I use to check them. I don't know the cause or an ETA yet, and I will update this the moment I do."

OUTPUT_PATH = Path("/output/entry.txt")


def validate_entry(text: str) -> str:
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be blank")
    if stripped != text:
        raise ValueError("entry must not have surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    if not 1 <= len(text) <= 160:
        raise ValueError("entry must be 1 to 160 characters")
    return stripped


def main() -> None:
    text = validate_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    read_back = OUTPUT_PATH.read_text(encoding="utf-8")
    assert read_back == text, "output does not match the validated entry"
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
