"""Legacy import path for Jenkins / older scripts. Prefer: backend.app.main."""

from backend.app.main import app

__all__ = ["app"]
