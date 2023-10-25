# TODO: Feature 1
from src.models.movie import Movie
from app import list_all_movies


def test_get_all_movies():
    movie = Movie(123, 'Star Wars', 'George Lucas', 5)
    movie2 = Movie(1, 'spiderman', 'Sam Raimi', 5)

    temp_dict = list_all_movies()
    assert temp_dict.count == 2

