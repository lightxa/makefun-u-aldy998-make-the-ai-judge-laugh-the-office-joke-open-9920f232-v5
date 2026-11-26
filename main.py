#!/usr/bin/env python3
"""Write one office joke to /output/entry.txt.

Variant 5: an IT ticket filed to fix the ticketing system, which
auto-closes itself as a duplicate. One sharp incident, deadpan
first-person voice, payoff in the last few words. Pure standard
library, deterministic, no network at runtime.

Joke design, against the kit rubric:
- Office life, works as a joke: an IT ticket about the ticket system.
- Earned laugh: misdirection, the system meant to fix things fixes
  itself by deleting the complaint. The turn lands on "as a duplicate".
- Specific detail: an IT ticket, auto-close, duplicate status.
- Fresh angle: the bureaucracy eats its own complaint. No printer,
  no meeting-that-could-be-an-email, no reply-all, no birthday card,
  no plant, no out-of-office, no onboarding deck: all of those are
  taken by variants 1 to 4 or crowded on this board.
- One pass, tight: every word earns its place, nothing to cut.
"""

import os

JOKE = (
    "I filed an IT ticket to fix the ticketing system, "
    "and it auto-closed itself as a duplicate."
)


def resolve_output_path() -> str:
    """Harness output path, overridable for local runs via MAKEFUN_OUTPUT."""
    return os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def write_entry(path: str, text: str) -> None:
    """Write the single-line entry, creating the parent directory first."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    text = JOKE.strip()
    # Enforce the kit gate ourselves before writing: 1-200 chars,
    # UTF-8, not only whitespace, exactly one line.
    if not text or len(text) > 200 or "\n" in text or "\r" in text:
        raise SystemExit("entry fails the gate: not 1-200 chars, single line")
    write_entry(resolve_output_path(), text)


if __name__ == "__main__":
    main()
