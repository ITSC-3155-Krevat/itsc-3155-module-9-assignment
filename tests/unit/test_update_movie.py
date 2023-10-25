# TODO: Feature 5
# first import the function we want to test via unit test
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie
from app import update_movie

sampleMovie = get_movie_repository()
movie = sampleMovie.create_movie('Sample Movie', 'Sample Director', 3)
id = movie.movie_id
# create our test function for unit testing


def test_edit_unit():
    sampleMovie.update_movie(id, 'New Movie', 'New Director', 1)
    assert movie.movie_id == id
    assert movie.title == 'New Movie'
    assert movie.director == 'New Director'
    assert movie.rating == 1

# Resources
# 3155 Discord
# https://www.youtube.com/watch?v=bToSg1TSpMA
