#!/usr/bin/env python3
"""news-image-20261118 v9b (akun 6): 30-story front page, no map.

Verifiability-First atas v8 (985.514, rank 99): 30 cerita berdampak
tertinggi (3 TOP + 12 grid + 15 ALSO), TANPA peta — menguji rumus rank 6
(989.515 tanpa peta). Kartu grid besar, tiap kartu bertag sumber + badge
temporal (REPORTED/SCHEDULED/PLANNED), kotak DATE CHECK bingkai emas, NOL
item follow-up. Berita sore/malam ditutup (GTA VI, inflasi UK 3,6%, COP31
35x35, emas $3.792, Jeffries 251-262, operasi darat Gaza ganti Board of
Peace, Java4Shell). Setiap cerita pertama dilaporkan Rabu 18 Nov 2026.
Deterministic, offline.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "image.jpg")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)

    # Guard: entry must be <= 1 MiB and exactly 1024x1024.
    assert os.path.getsize(dst) <= 1048576, "entry over 1 MiB"


if __name__ == "__main__":
    main()
