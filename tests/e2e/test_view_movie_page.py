#Anessa's get_single_movie test e2e feature
# Feature 4

import pytest
from app import app, movie_repository
from src.models.movie import Movie
from flask.testing import FlaskClient

def test_view_movie_page(test_app: FlaskClient):
    movie_repository.clear_db()
    movie = movie_repository.create_movie('Parasite', 'Bong Joon-ho', 5)
    response = test_app.get(f'/movies/{movie.movie_id}', follow_redirects=True)
    response_data = response.data.decode('utf-8')
    if f'<h4>f"Movie with id: {movie.movie_id} not found."</h4>' in response_data:
        assert '<h4>{{ error_message }}</h4>' in response_data
    else:
        assert f'<h4>f"Movie with id: {movie.movie_id} not found."</h4>' not in response_data

def test_get_single_movie_without_id(test_app: FlaskClient):
    movie_repository.clear_db()
    response = test_app.get('/get_single_movie', data={
        'title': 'Parasite',
        'director': 'Bong Joon-ho',
        'rating': 5
    }, follow_redirects=True)
    assert response.status_code == 404

def test_view_movie_page_validation_error(test_app: FlaskClient):
    movie_repository.clear_db()
    movie_id = 9999
    response = test_app.get(f'/movies/{movie_id}')
    assert response.status_code != 404