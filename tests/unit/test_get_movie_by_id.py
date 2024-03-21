#Anessa's get_single_movie test unit feature
# Feature 4

import pytest
from flask import redirect
from app import app, movie_repository
from src.models.movie import Movie

@pytest.fixture(scope='module')
def client():
    with app.test_client() as client:
        yield client

def test_get_movie(client):
    movie_repository = Movie(123, 'Star Wars', 'George Lucas', 5)
    assert movie_repository.movie_id == 123
    response = client.get(f'/movies/{movie_repository.movie_id}', data = {
        'title': movie_repository.title,
        'director': movie_repository.director,
        'rating': movie_repository.rating
    }, follow_redirects=True)
    response_data = response.data.decode('utf-8')
    if response.status_code != 200:
        assert f'<h4>f"Movie with id: {movie_repository.movie_id} not found."</h4>' in response_data
        assert '<h2 name="title">Star Wars</h2>' not in response_data
    elif response.status_code == 200:
        assert f'<h4>f"Movie with id: {movie_repository.movie_id} not found."</h4>' not in response_data

def test_movie_id_validation_error(client):
    movie_id = 9999
    response = client.get(f'/movies/{movie_id}')
    assert response.status_code != 404
