"""Lightweight checks for CI (no server, no interactive CLI). Run from repo root."""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))


def main() -> int:
    from backend.app.main import app

    assert app.title
    import frontend.fastapi_app as legacy

    assert legacy.app is app
    print("OK:", app.title)
    return 0


if __name__ == "__main__":
    sys.exit(main())
