#Anessa's get_single_movie test unit feature
# Feature 4

import pytest
from app import app, movie_repository
from src.models.movie import Movie

@pytest.fixture(scope='module')
def client():
    with app.test_client() as client:
        yield client

def test_get_movie_by_id(client):
    movie_repository.clear_db()
    movie = Movie(123, 'Star Wars', 'George Lucas', 5)
    response = client.get(f'/movies/{movie.movie_id}', follow_redirects=True)
    assert movie.movie_id == 123
    assert response.status_code == 200


def test_movie_id_validation_error(client):
    movie_repository.clear_db()
    movie_id = 9999
    response = client.get(f'/movies/{movie_id}')
    assert response.status_code != 404
