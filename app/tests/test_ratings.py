from fastapi.testclient import TestClient
from ..main import app
from ..models import Rating

client = TestClient(app)

def test_rate_chapter():
    rating = Rating(course_name="Highlights of Calculus", chapter_name="Big Picture of Calculus", rating=1)
    response = client.post("/ratings/", json=rating.dict())
    assert response.status_code == 200
    assert response.json()['message'] == "Rating added successfully"
