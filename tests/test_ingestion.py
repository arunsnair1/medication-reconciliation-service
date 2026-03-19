from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ingest_medications():
    response = client.post(
        "/patients/999/medications",
        json={
            "source": "clinic_emr",
            "medications": [
                {
                    "name": "aspirin",
                    "dose": 100,
                    "unit": "mg",
                    "status": "active"
                }
            ]
        }
    )

    assert response.status_code == 200
    assert "version" in response.json()