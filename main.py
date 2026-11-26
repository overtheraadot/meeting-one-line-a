"""make.fun entry: The Meeting That Should Have Been One Line (meeting-one-line-a).

Writes the single sentence that could have replaced an entire
pointless meeting to /output/entry.txt and prints a short report.

Gate (from the kit RULES.txt): the file must be UTF-8 text of 1 to 200
characters, not only white space. The entry is a single line.

The line: the meeting could have been an email, but the email would
have needed a meeting to explain it. It kills the meeting completely,
loops back on itself like the meeting did, and is recognizable to
anyone who has sat through a useless one. No context, no explanation:
the sentence is the whole replacement.
"""

import os

# The entry: one line, my own invention. A meeting about the email.
ENTRY = (
    "This meeting could have been an email, but the email would have "
    "needed a meeting to explain it."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def verify(text):
    """Enforce the gate from RULES.txt: 1-200 chars, non-blank, one line.

    Also rejects leading/trailing whitespace: the judged text is the
    line itself, so stray spaces would count against the limit and
    look sloppy on the leaderboard.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d chars, over the %d-char limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    return True


def write_entry(path=OUTPUT_PATH):
    """Validate the entry, then write it exactly as-is, no newline."""
    verify(ENTRY)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def report(path):
    """Read the written file back and print its length and headroom."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    headroom = MAX_CHARS - len(text)
    print("Wrote %s (%d chars, %d line(s), %d chars of headroom)"
          % (path, len(text), text.count("\n") + 1, headroom))
    print(text)
    return text


def main():
    report(write_entry())


if __name__ == "__main__":
    main()
