# TODO: Feature 4
import pytest
from app import app
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_single_movie(client):
    movie_repository = get_movie_repository()
    movie_repository.create_movie("The Movie Title", "Director", 5)

    response = client.get('/movies/5')

    assert b'The Movie Title' in response.data
    assert b'Director' in response.data
    assert b'5' in response.data

def test_search_movie_not_found(client):
    response = client.get('/movies/6')
    assert b'Cannot find movie' in response.data