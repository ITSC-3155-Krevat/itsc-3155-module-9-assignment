# Feature 3
from app import app
from src.repositories.movie_repository import get_movie_repository

def test_search_movies():
    test_app = app.test_client()

    # No query
    response = test_app.get('/movies/search')
    assert response.status_code == 200
    assert b'<p class="mb-3">Search for a movie rating below by its title!</p>' in response.data

    # Real query
    get_movie_repository().create_movie('Test Movie', 'Test Director', 3)
    response = test_app.get('/movies/search?title=Test+Movie')
    assert response.status_code == 200
    assert b'<p class="mb-3">Test Movie has a rating of 3 stars</p>'

    # Fake query
    response = test_app.get('/movies/search?title=Fake+Movie')
    assert response.status_code == 200
    assert b'<p class="mb-3">Search for a movie rating below by its title!</p>' in response.data
