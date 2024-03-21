# TODO: Feature 5
import pytest
from src.repositories.movie_repository import get_movie_repository


@pytest.fixture
def movie_repo():
    repo = get_movie_repository()
    repo.clear_db()  # Ensuring a clean state before each test
    return repo


def test_update_movie_success(movie_repo):
    # Creating a movie to update
    movie = movie_repo.create_movie("Titanic", "Director", 5)
    # Updating the movie
    updated_movie = movie_repo.update_movie(movie.id, "Sunken Titanic", "Director Name", 4)
    # Asserting the changes
    assert updated_movie.title == "New Title"
    assert updated_movie.rating == 4


def test_update_movie_failure(movie_repo):
    # Attempting to update a movie that does not exist, resulting in a failure
    with pytest.raises(ValueError):
        movie_repo.update_movie(999, "New Movie", "Director Name", 3)


