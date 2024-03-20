import pytest
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture
def movie_repo():  # create and clear the movie repository
    repo = get_movie_repository()
    repo.clear_db()
    return repo

def test_movie_success(movie_repo):  # test retrieving a movie successfully
    created_movie = movie_repo.create_movie("Inception", "Christopher Nolan", 8)  # create a mock movie
    fetched_movie = movie_repo.get_movie_by_id(created_movie.movie_id)  # fetch the created movie by id
    
    # make sure the fetched movie matches the created movie
    assert fetched_movie is not None
    assert fetched_movie.title == "Inception"
    assert fetched_movie.director == "Christopher Nolan"
    assert fetched_movie.rating == 8

def test_movie_failed(movie_repo):  # test failure to retrieve a non-existent movie
    movie_repo.clear_db()  # no movie exists with the id
    fetched_movie = movie_repo.get_movie_by_id(999)  # fetch a movie by a non-existent id
    
    assert fetched_movie is None