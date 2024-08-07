from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_get_chapter():
    response = client.get("/chapters/Highlights of Calculus/Big Picture of Calculus")
    assert response.status_code == 200
    assert response.json()['name'] == "Big Picture of Calculus"
