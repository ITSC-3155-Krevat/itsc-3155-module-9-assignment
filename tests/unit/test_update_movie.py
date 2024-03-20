# TODO: Feature 5
from flask.testing import FlaskClient
from app import app
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_update_movie():
    movie_repository.create_movie('Spiderman', 'Ronni', 5,)
    spiderman_movie = movie_repository.get_movie_by_title('Spiderman')
    movie_repository.update_movie(spiderman_movie.movie_id,'Superman', 'Ronni E', 4,)

    assert spiderman_movie.title == 'Superman'
    assert spiderman_movie.director == 'Ronni E'
    assert spiderman_movie.rating == 4