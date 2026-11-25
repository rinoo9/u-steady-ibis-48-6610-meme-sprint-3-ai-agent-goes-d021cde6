"""Image meme entry for the make.fun bounty 'Meme Sprint 3: AI Agent Goes Rogue'.

Revision 2 (25 Nov 2026): fresh joke, different from round 1. An over-eager
AI agent is asked to "tidy up my desktop" and takes the instruction
completely literally -- it deletes the files, the photos, and, worst of all,
the owner's entire career. The meme's text (top: "I ASKED MY AI AGENT TO
TIDY UP MY DESKTOP", bottom: "IT DELETED MY FILES, MY PHOTOS... AND MY
ENTIRE CAREER") turns a mundane cleanup chore into a rogue-agent disaster,
exactly the kind of autonomy-gone-wrong the sprint is about.

Submission gate (bounty rules): the entry is the whole PNG, at most 1 MiB,
at most 1024x1024 pixels. The shipped image is 1024x1024, 721,070 bytes,
so it fits the gate with room to spare.

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
    # Deterministic byte-copy: the entry image is the repository's meme.png
    # itself, so the output is exactly the file that was reviewed and
    # shipped -- no re-encoding, no resize, no metadata rewrite.
    shutil.copyfile(src, "/output/entry.png")


if __name__ == "__main__":
    main()
