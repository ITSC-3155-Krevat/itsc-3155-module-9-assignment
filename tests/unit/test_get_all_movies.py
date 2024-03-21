# TODO: Feature 1
import pytest
from src.repositories.movie_repository import get_movie_repository, MovieRepository

# Assuming you have a MovieRepository class, you can use pytest fixtures to initialize it
@pytest.fixture
def movie_repository():
    # If there's any setup needed for the repository, do it here
    repo = get_movie_repository()
    return repo

# Happy path where the repository has movies
def test_get_all_movies_with_data(movie_repository):
    # Setup - add some mock movies to the repository
    movie_repository.add_movie({'title': 'Movie 1', 'director': 'Director 1', 'rating': 8})
    movie_repository.add_movie({'title': 'Movie 2', 'director': 'Director 2', 'rating': 7})

    # Exercise - get all movies
    movies = movie_repository.get_all_movies()

    # Verify - check that all mock movies are in the result
    assert len(movies) == 2
    assert movies[0].title == 'Movie 1'
    assert movies[1].title == 'Movie 2'

    # Teardown - remove mock data if necessary
    movie_repository.clear_db()

# Edge case where the repository has no movies
def test_get_all_movies_with_no_data(movie_repository):
    # Exercise - get all movies from an empty repository
    movies = movie_repository.get_all_movies()

    # Verify - check that the result is empty
    assert len(movies) == 0

