# TODO: Feature 3
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository


def test_get_movie_by_title():
    
    movie_repository = get_movie_repository()

    existing_movie = Movie(movie_id=3, title="The Godfather", director="Francis Ford Coppola", rating=4)
    movie_repository.create_movie(existing_movie.title, existing_movie.director, existing_movie.rating)

    movie = movie_repository.get_movie_by_title(existing_movie.title)
    assert movie.title == existing_movie.title
    assert movie.director == existing_movie.director
    assert movie.rating == existing_movie.rating

    movie = movie_repository.get_movie_by_title("Non-existent Movie")
    assert movie is None


