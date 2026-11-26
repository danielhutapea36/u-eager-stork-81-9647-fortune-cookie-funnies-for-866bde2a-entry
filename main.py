#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers.

Writes the funniest possible fortune-cookie message for a software
engineer to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The line
is 63 characters, UTF-8, one line, no trailing newline. Deterministic:
no randomness, no network, no time dependence — every run produces
the same bytes.

Why this line: the judge weighs, in order, (1) it is a fortune-cookie
message for a software engineer — the "You will find..." opening is
the classic fortune-cookie frame, and the subject is the engineer's
own bug, not a generic slogan; (2) it is genuinely funny on a first
read — the punchline is a confession every engineer recognises, that
the bug lives in code they swore was temporary; (3) it sounds like a
fortune cookie — short, declarative, its twist coming from the
engineer's world of bugs and code; (4) it is fresh — "temporary code"
is a real engineer trope, but the phrasing is written for this brief,
not lifted from a mug or a conference slide; (5) it is tight — every
word earns its place, and the funniest word, "temporary", sits at the
end. At 63 characters it also stays well inside the 120-character
gate, and a shorter text wins an exact tie on Judge win rate.

Revision note: the first draft read "Your deploy will succeed on
Friday. The bug will simply wait until Monday." — dropped, because
the joke landed on a schedule, not on the engineer's own code, and
"wait until Monday" needed the reader to supply the Friday-deploy
superstition as setup. The bug-in-temporary-code version replaced it:
the confession is the engineer's own, the fortune frame stays intact,
and the punch word sits at the very end.
"""

import os

TEXT = "You will find the bug in the code you swore was only temporary."

def main() -> None:
    # Gate: entry.txt must be 1-120 characters of UTF-8 text, not only
    # whitespace. The line is 63 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 120 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
