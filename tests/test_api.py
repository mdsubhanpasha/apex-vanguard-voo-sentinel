from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["system"] == "APEX-VANGUARD-VOO-SENTINEL-4050"
    assert "WhatsApp" in data["contact"]

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "HEALTHY"

def test_analyze_endpoint():
    response = client.post("/analyze")
    assert response.status_code == 200
    data = response.json()
    assert data["duplicate_count"] == 6
    assert data["total_leakage_prevented_usd"] == 702.90
