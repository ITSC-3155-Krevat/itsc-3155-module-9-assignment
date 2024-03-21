# TODO: Feature 3

from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_get_title():
    movie_repository.create_movie("My_movie", "Myself", 80)
    result = movie_repository.get_movie_by_title("My_movie")
    assert result.director == "Myself"
    assert result.rating == 80
    assert result.title == "My_movie"