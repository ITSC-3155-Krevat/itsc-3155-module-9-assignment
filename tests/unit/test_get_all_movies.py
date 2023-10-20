# TODO: Feature 1
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_get_all_movies():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    assert len(movie_repository.get_all_movies()) == 0
    movie_repository.create_movie("movie1","John1",1)
    assert len(movie_repository.get_all_movies()) == 1
    data = movie_repository.get_all_movies()
    for id in data:
        assert movie_repository.get_movie_by_id(id).title == "movie1"
        assert movie_repository.get_movie_by_id(id).director == "John1"
        assert movie_repository.get_movie_by_id(id).rating == 1


