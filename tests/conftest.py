import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from backend.app.main import app  # noqa: E402

@pytest.fixture
def client():
    """FastAPI TestClient fixture."""
    # Override paths for test data (assume data/ exists)
    return TestClient(app)

@pytest.fixture
def sample_symptoms():
    """Sample symptoms for testing."""
    return "itching,skin_rash"

