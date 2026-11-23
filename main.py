#!/usr/bin/env python3
"""Copy the front page beside this script to $MAKEFUN_OUTPUT_DIR/entry.png."""
import hashlib
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(ROOT, "entry.png")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    size = os.path.getsize(dest)
    src_hash = sha256(SOURCE)
    dest_hash = sha256(dest)
    print(f"wrote {size} bytes to {dest}")
    print(f"sha256 {dest_hash}")
    if src_hash != dest_hash:
        print(f"hash mismatch: source {src_hash}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
