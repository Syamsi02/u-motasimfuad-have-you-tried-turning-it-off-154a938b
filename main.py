"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line from a hopeless tech support agent to a
desperate customer, to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Pure standard library, deterministic: the same line every run.
"""

import os

LINE = (
    "Have you tried turning it off and on again? Mine's been "
    "restarting since Tuesday — if it works for you, call me "
    "back and tell me how."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
