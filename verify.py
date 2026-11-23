#!/usr/bin/env python3
"""Verify all delivered files against SHA256SUMS."""
from pathlib import Path
import hashlib
import sys
root = Path(__file__).resolve().parent
manifest = root / "SHA256SUMS"
failures = []
for line in manifest.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    expected, name = line.split("  ", 1)
    path = root / name
    if not path.is_file():
        failures.append(f"MISSING: {name}")
        continue
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        failures.append(f"MISMATCH: {name}")
if failures:
    print("\n".join(failures))
    sys.exit(1)
print("PASS: all delivered files match SHA256SUMS.")
