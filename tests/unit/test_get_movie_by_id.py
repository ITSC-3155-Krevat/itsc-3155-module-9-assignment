# TODO: Feature 4
import pytest
from src.repositories.movie_repository import get_movie_repository

repo = get_movie_repository()

def test_id_search():
    movie = repo.create_movie("The Room", "Tommy", 5)
    id = movie.movie_id
    found = repo.get_movie_by_id(id)
    assert found is not None
    found = repo.get_movie_by_id(0)
    assert found is None
