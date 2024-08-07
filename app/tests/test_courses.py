from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_get_courses():
    response = client.get("/courses/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_course_overview():
    response = client.get("/courses/Highlights of Calculus")
    assert response.status_code == 200
    assert response.json()['name'] == "Highlights of Calculus"
