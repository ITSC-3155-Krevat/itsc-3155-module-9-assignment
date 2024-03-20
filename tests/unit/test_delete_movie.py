# Feature 6
# Nhu's unit testing
from src.repositories.movie_repository import get_movie_repository
from app import movie_repository
import pytest

def test_delete_movie_id():
    movie_repository.clear_db()
    # create a movie
    movie1 = movie_repository.create_movie("Finding Nemo", "Bob", 5)
    movies = movie_repository.get_all_movies()
    assert len(movies) == 1
    # delete the movie
    movie_repository.delete_movie(movie1.movie_id)
    # test if the size changes after deleting the movie
    movies = movie_repository.get_all_movies()
    assert len(movies) == 0

def test_delete_movie_no_id():
    movie_repository.clear_db()
    # create a movie
    movie1 = movie_repository.create_movie("Finding Nemo", "Bob", 5)
    movie_id = 999
    # delete a movie with movie_id not exist
    with pytest.raises(ValueError):
        movie_repository.delete_movie(movie_id)
    movies = movie_repository.get_all_movies()
    # test if the size still the same
    assert len(movies) == 1
