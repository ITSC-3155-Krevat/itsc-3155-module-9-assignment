# TODO: Feature 5
from flask.testing import FlaskClient
from app import app
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_update_movie():
    movie_repository.create_movie('Spiderman', 'Ronni', 5,)
    movie = movie_repository.get_movie_by_title('Spiderman')
    assert movie.title == 'Spiderman'
    assert movie.rating == 5
    movie_repository.update_movie(movie.movie_id,'Superman', 'Ronni E', 4,)

    assert movie.title == 'Superman'
    assert movie.title != 'Deadpool'
    assert movie.director == 'Ronni E'
    assert movie.rating == 4
    assert movie.director != 'Ronni'
    assert movie.rating != '1'

