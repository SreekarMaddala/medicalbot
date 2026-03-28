import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest
from fastapi.testclient import TestClient

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from backend.app.main import (  # noqa: E402
    get_predicted_value,
    helper,
    symptoms_dict,
)


@pytest.mark.api
class TestMedicalApp:
    def test_get_symptoms(self, client: TestClient):
        """Test GET /api/symptoms returns symptom list."""
        response = client.get("/api/symptoms")
        assert response.status_code == 200
        data = response.json()
        assert "symptoms" in data
        assert isinstance(data["symptoms"], list)
        assert len(data["symptoms"]) == len(symptoms_dict)
        assert "itching" in data["symptoms"]

    @pytest.mark.ml
    def test_predict_api_fungal(self, client: TestClient, sample_symptoms: str):
        """Test prediction with fungal infection symptoms (real model)."""
        response = client.post("/api/predict", data={"symptoms": sample_symptoms})
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["disease"] == "Fungal infection"
        assert len(data["precautions"]) == 4
        assert len(data["medications"]) >= 1

    def test_predict_api_no_symptoms(self, client: TestClient):
        """Missing/empty symptoms returns JSON error."""
        response = client.post("/api/predict", data={"symptoms": ""})
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is False
        assert "error" in data

    def test_home_page(self, client: TestClient):
        """Test root endpoint loads home template context."""
        response = client.get("/")
        assert response.status_code == 200
        assert b"symptom" in response.content.lower()

    def test_about_page(self, client: TestClient):
        """Test about page."""
        response = client.get("/about")
        assert response.status_code == 200

    @patch("backend.app.main.svc")
    def test_get_predicted_value(self, mock_svc: MagicMock, sample_symptoms: str):
        """Unit test prediction function with mocked model."""
        mock_svc.predict.return_value = [15]  # Fungal infection in diseases_list
        psyms = [s.strip().lower() for s in sample_symptoms.split(",")]
        result = get_predicted_value(psyms)
        assert result == "Fungal infection"
        mock_svc.predict.assert_called_once()

    @patch("pandas.read_csv")
    def test_helper_mock(self, mock_read_csv: MagicMock):
        """Smoke test helper with dataframe-backed mocks (unused path; helper uses real CSVs)."""
        mock_read_csv.return_value = pd.DataFrame(
            {"Disease": ["Fungal infection"], "Description": ["Test desc"]}
        )
        desc, pre, med, die, wrk = helper("Fungal infection")
        assert isinstance(desc, str)
        assert len(pre) == 4

