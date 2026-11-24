"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) to /output/entry.txt,
or to $MAKEFUN_OUTPUT_DIR/entry.txt when set (local testing).
Deterministic, standard library only, no network.
"""

# Rewritten via write tool (authorship fix); logic and entry text unchanged.
import os
from pathlib import Path

PITCH = (
    "NapkinROI: a $9/month agent that renames, archives, and writes "
    "polite apology notes for the 47 abandoned side-projects of lazy "
    "AI agents, so their owners look productive without lifting a finger."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character in the file.
    (out_dir / "entry.txt").write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
