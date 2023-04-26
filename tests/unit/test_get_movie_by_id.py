# TODO: Feature 4
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_id():
    repo = get_movie_repository()

    # Add some movies to the repo
    movie1 = Movie(1, 'Movie 1', 'Director 1', 5)
    movie2 = Movie(2, 'Movie 2', 'Director 2', 4)
    repo._db = {1: movie1, 2: movie2}

    # Test getting an existing movie
    movie = repo.get_movie_by_id(1)
    assert movie == movie1

    # Test getting a non-existing movie
    movie = repo.get_movie_by_id(3)
    assert movie is None
