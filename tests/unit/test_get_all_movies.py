# TODO: Feature 1
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie
from app import list_all_movies

def test_get_all_movies():
    get_movie_repository().create_movie('Movie Name', 'Director Name', 1)
    movie = get_movie_repository().get_all_movies()

