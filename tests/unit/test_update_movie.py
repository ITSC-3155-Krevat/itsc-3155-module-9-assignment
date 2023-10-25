# TODO: Feature 5
from flask.testing import FlaskClient
import pytest
from app import app
from src.repositories.movie_repository import get_movie_repository


def test_update_movie() -> None:

    # create a movie
    movie_repo = get_movie_repository()
    movie_repo.clear_db()
    movie_repo.create_movie('Test Movie', 'Test Director', 5)
    movie = movie_repo.get_movie_by_title('Test Movie')

    assert len(movie_repo.get_all_movies()) == 1
    assert movie is not None
    # update movie
    movie_repo.update_movie(movie.movie_id, 'Test Movie 2', 'Test Director 2', 3)
    movie2 = movie_repo.get_movie_by_title('Test Movie 2')
    assert movie2 is not None
    assert len(movie_repo.get_all_movies()) == 1
    assert movie_repo.get_movie_by_title('Test Movie') is None
    assert movie_repo.get_movie_by_title('Test Movie 2') is not None