# TODO: Feature 6
import pytest
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie
def test_add_movie():
    movies=get_movie_repository()
    movies.create_movie("Saw X","Kevin Greutert", 4)
    result = movies.get_movie_by_title("Saw X")
    assert result is not None
    assert result.title == "Saw X"
    assert isinstance(result, Movie)

def test_delete_movie():
    movies=get_movie_repository()
    movies.create_movie("Saw X","Kevin Greutert", 4)
    result = movies.get_movie_by_title("Saw X")
    # assert isinstance(result, Movie)
    assert result is not None
    assert result.title == "Saw X"
    # movies.delete_movie()
    assert not isinstance(result, Movie)

def test_deleted_selected_movie():
    movies=get_movie_repository()
    result = movies.get_movie_by_title("Inception")
    # assert isinstance(result, Movie)
    # movies.delete_movie()
    assert not isinstance(result, Movie)
    assert result is not None
    result = movies.get_movie_by_title("Dark Knight")
    assert isinstance(result, Movie)
    assert result is not None
    result = movies.get_movie_by_title("Intersellar")
    assert isinstance(result, Movie)
    assert result is not None
    result = movies.get_movie_by_title("The Shawshank Redemption")
    assert isinstance(result, Movie)
    assert result is not None
    result = movies.get_movie_by_title("The Matrix")
    assert isinstance(result, Movie)