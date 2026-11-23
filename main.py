"""Image meme entry for the make.fun bounty 'Meme Sprint 3: AI Agent Goes Rogue'.

Writes the shipped meme image to /output/entry.png.
Deterministic: no network, no randomness, no environment reads.
The image lives in this repository as meme.png and is copied byte for byte.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    src = os.path.join(HERE, "meme.png")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(src, "/output/entry.png")


if __name__ == "__main__":
    main()
