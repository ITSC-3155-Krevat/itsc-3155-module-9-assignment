# TODO: Feature 3

from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie
from app import app

movie = get_movie_repository()
movie.create_movie('Toy Story', 'John Lasser', 3)

def test_search_movies():
    test_app = app.test_client()
    response = test_app.get('/movies/search')
    assert b'<p class="mb-3">Search for a movie rating below</p>' in response.data

def test_search_movies_with_movie():
    test_app = app.test_client()
    response = test_app.get('/movies/search?searched=Toy+Story')
    print(response.data)
    assert b'<h2 class="text-center">Found your movie!</h2>' in response.data
    assert b'<th>Toy Story</th>' in response.data

def test_search_movies_with_wrong_movie():
    test_app = app.test_client()
    response = test_app.get('/movies/search?searched=toyStroy')
    assert b'<h2 class="text-center">Could not find your movie</h2>' in response.data
