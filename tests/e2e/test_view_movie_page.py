# TODO: Feature 4
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository
from flask.testing import FlaskClient
import json

def test_view_movie_page(client: FlaskClient):
    # Create a movie in the repo
    repo = get_movie_repository()
    movie = Movie(1, 'Movie1', 'Director1', 5)
    repo._db = {1: movie}

    # Test viewing an existing movie
    response = client.get('/movies/1')
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    # assert json.loads(response.data) == movie.__dict__
    response_data = response.data
    assert b'<h1 class="mb-5">Movie1 , Director1, 5</h1>' in response_data

    # Test viewing a non-existing movie
    
    response = client.get('/movies/2')
    assert response.status_code == 404
    assert response.headers['Content-Type'] == 'application/json'
    # assert json.loads(response.data) == {'message': 'Movie not found'}
    assert '<h1 class="mb-5">Movie not found</h1>' in response.data
