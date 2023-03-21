import pytest
from app import app
from src.repositories.movie_repository import get_movie_repository

# TODO: Feature 1 [DONE]
def test_all_movies_page():
    test_app = app.test_client()
    response = test_app.get('/movies')
    assert response.status_code == 200
    assert b'<td colspan="3">No movies found</td>' in response.data

def test_show_movie():
    test_app = app.test_client()
    movie_repository = get_movie_repository()
    movie_repository.create_movie('The Matrix', 'Wachowski', 5)
    response = test_app.get('/movies')
    assert response.status_code == 200
    assert b'<td>The Matrix</td>' in response.data
