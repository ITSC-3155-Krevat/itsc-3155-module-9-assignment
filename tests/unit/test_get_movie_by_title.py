# TODO: Feature 3

import pytest
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

@pytest.fixture
def movie_repository():
    movie_repo = get_movie_repository()
    movie_repo.clear_db()
    return movie_repo

def test_get_movie_by_title_existing(movie_repository):
    movie_repository.create_movie("The Movie Title", "Director", 5)

    movie = movie_repository.get_movie_by_title("The Movie Title")

    assert movie is not None
    assert movie.title == "The Movie Title"
    assert movie.director == "Director"
    assert movie.rating == 5

def test_get_movie_by_title_not_found(movie_repository):
    movie = movie_repository.get_movie_by_title("Non-Existent Title")

    assert movie is None
