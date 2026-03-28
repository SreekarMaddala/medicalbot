"""CLI entry point at repo root (delegates to scripts/run_medical_system.py)."""

from __future__ import annotations

import runpy
import sys
from pathlib import Path

if __name__ == "__main__":
    target = Path(__file__).resolve().parent / "scripts" / "run_medical_system.py"
    sys.argv[0] = str(target)
    runpy.run_path(str(target), run_name="__main__")
