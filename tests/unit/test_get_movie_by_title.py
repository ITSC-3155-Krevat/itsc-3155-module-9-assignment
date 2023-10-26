# TODO: Feature 3
import pytest
from src.repositories.movie_repository import get_movie_repository
movie_repository = get_movie_repository()

def test_search():
    movie_repository.create_movie("shrek","beans",4)
    result = movie_repository.get_movie_by_title("shrek")
    assert result is not None
    result = movie_repository.get_movie_by_title("shrark")
    assert result is None



