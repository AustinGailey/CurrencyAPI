from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Currency API"}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_currency():
    response = client.get("/USD")
    assert response.json().data.currency == "USD"
