# TODO: Feature 1
import pytest
from app import app
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture()
def test_app():
    return app.test_client()

def test_all_movies_page(test_app):
    response = test_app.post("/movies", data={
        "title": "Toy Story",
        "director": "John Lasster",
        "rating": "3",
    })
    response = test_app.get('/movies')
    print(response.data)
    assert response.status_code == 200
    assert b'<td>Toy Story</td>' in response.data
    assert b'<td>John Lasster</td>' in response.data
    assert b'<td>3</td>' in response.data

    
    
