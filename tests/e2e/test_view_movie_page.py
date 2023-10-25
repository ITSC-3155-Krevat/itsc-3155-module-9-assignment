# TODO: Feature 4

from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository

def test_view_movie_page(client):
    repo = get_movie_repository()
    movie = Movie(1, 'Movie1', 'Director1', 5)
    repo._db = {1: movie}
    
    response = client.get('/movies/1')
    assert response.status_code == 200
    assert 'Movie Details' in response.data.decode('utf-8')
    assert 'Movie1' in response.data.decode('utf-8')
    
    response = client.get('/movies/2')
    assert response.status_code == 404
    assert 'Movie not found' in response.data.decode('utf-8')
