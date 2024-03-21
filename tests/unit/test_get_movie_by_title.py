# TODO: Feature 3
import pytest
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture
def movie_repo():
    repo = get_movie_repository()
    repo.clear_db()  # Assuming clear_db is implemented
    return repo

def test_get_movie_by_title_exists(movie_repo):
    # Add a movie to the repository
    movie_repo.create_movie("Test Movie", "Test Director", 5)
    # Attempt to retrieve the added movie
    movie = movie_repo.get_movie_by_title("Test Movie")
    assert movie is not None
    assert movie.title == "Test Movie"
    assert movie.director == "Test Director"
    assert movie.rating == 5

def test_get_movie_by_title_not_exists(movie_repo):
    # Ensure that searching for a non-existing movie returns None
    movie = movie_repo.get_movie_by_title("Non-Existent Movie")
    assert movie is None
