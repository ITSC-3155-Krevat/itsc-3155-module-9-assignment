# Feature 6
# Nhu's e2e testing
from app import app, movie_repository
import pytest
from flask.testing import FlaskClient

from src.repositories.movie_repository import get_movie_repository

def test_delete_movie(test_app: FlaskClient):
    movie_repository.clear_db()
    movie1 = movie_repository.create_movie("Finding Nemo", "Bob", 5)
    movie_repository.delete_movie(movie1.movie_id)
    response = test_app.get('/movies')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert b'Finding Nemo' not in response.data

def test_delete_movie_id_not_exist(test_app: FlaskClient):
    movie_repository.clear_db()
    movie_id = 999
    with pytest.raises(ValueError):
        movie_repository.delete_movie(movie_id)
    response = test_app.get(f'/movies/{movie_id}/delete')
    assert response.status_code == 405



