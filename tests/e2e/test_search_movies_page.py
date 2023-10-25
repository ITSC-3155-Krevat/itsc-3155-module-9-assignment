# TODO: Feature 3
from flask.testing import FlaskClient
import pytest
from app import app
from src.repositories.movie_repository import get_movie_repository
movie_repository = get_movie_repository()


@pytest.fixture()
def test_app():
    return app.test_client()

def test_basic_func(test_app):
    response = test_app.get('/movies/search')
    assert response.status_code == 200
    assert b'<h1 class="mb-5">Search Movie Ratings</h1>' in response.data 


def test_search_movie(test_app):
    movie_repository.create_movie('chicken','rice',5)
    response = test_app.get('/movies/search?movieName=chicken')
    assert response.status_code == 200
    assert b'<p>Title: chicken</p>' in response.data


