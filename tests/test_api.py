from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_book():
    # Create a book
    response = client.post("/books/", json={"title": "Test Book", "description": "Testing FastAPI"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Book"

    # Get all books
    response = client.get("/books/")
    assert response.status_code == 200
    assert any(book["title"] == "Test Book" for book in response.json())

