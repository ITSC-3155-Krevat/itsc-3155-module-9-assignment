# TODO: Feature 4 As a user, I should be able to view a movie in isolation and have access to edit and delete that movie. There is no csv file for this feature.

from app import app
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_id():
    movie_repository = get_movie_repository()
    movie = Movie(1, "John Wich 4", "Me", 5)
    movie_repository.get_movie_by_id(movie)
    assert movie.movie_id == 1
    assert type(movie) == Movie
    
    