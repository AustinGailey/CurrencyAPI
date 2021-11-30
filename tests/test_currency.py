from fastapi.testclient import TestClient
from services.currency import app

client = TestClient(app)

def test_root():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() ==  {"status_code": "200"} 
