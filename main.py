#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers entry.

Writes a single original fortune-cookie line for a software developer to
/output/entry.txt:

    The code you wrote at 2 a.m. will review you at 9 a.m.

The line is one balanced sentence of 54 characters, well inside the
120-character gate. It is true about a developer's day -- late-night code
meets the morning code review -- and it turns that truth around: the code
you wrote reviews *you*, not the other way round. The quiet twist is the
role reversal, and the second read lands on the 2 a.m. / 9 a.m. mirror:
the hours are seven apart, but the judgement is the same code.
"""

import os

FORTUNE = "The code you wrote at 2 a.m. will review you at 9 a.m."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
