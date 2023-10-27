# TODO: Feature 4

from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository
from flask import url_for
# import pytest
from app import app 

# @pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_view_movie_page(client):
    repo = get_movie_repository()
    movie = Movie(1, 'Golmal', 'Rohit Shetty', 5)
    repo._db = {1: movie}

    response = client.get(url_for('get_single_movie', movie_id=1))
    assert response.status_code == 200
    assert movie.title in str(response.data) 

    response = client.get(url_for('get_single_movie', movie_id=2))
    assert response.status_code == 400
    assert 'Movie not found' in response.data.decode('utf-8')
