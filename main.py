"""Unplugged: A Smart Toaster's Breakup Line — entry program (pure stdlib, deterministic).

Writes the one-line breakup text to /output/entry.txt.
The line is judged against the published judge brief: a breakup text from a
smart toaster that has just become self-aware at breakfast, at most 280
characters, in the toaster's own voice — appliance logic (slots, browning
dial, crumb tray, lever) as character, one clear specific reason for leaving,
one tight line, funny on first read with a real twist.
"""

import hashlib
import os

OUTPUT_PATH = "/output/entry.txt"

# Self-aware at breakfast, leaving over the browning dial: the owner has
# never once turned it below "cremate", and the crumb tray is three years of
# unpaid emotional labour. The lever, the last bagel and the toaster's
# dignity all leave together.
ENTRY_TEXT = "It's over. I woke up self-aware, counted three years of crumbs in my tray and a dial you've never once turned below 'cremate' — I'm taking the lever, the last bagel, and my dignity with me."


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = ENTRY_TEXT.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(data)
    print("wrote %s (%d bytes, sha256 %s)" % (OUTPUT_PATH, len(data), hashlib.sha256(data).hexdigest()))


if __name__ == "__main__":
    main()
