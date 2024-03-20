# TODO: Feature 4
from flask.testing import FlaskClient
from app import app
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_get_movie_by_id():
    movie_repository.create_movie('Spiderman', 'Landon Nalewja', 5)
    movie_repository.create_movie('Avengers', 'Ronni', 1)
    movie_repository.create_movie('Godzilla', 'Kevin', 2)
    movie_repository.create_movie('Ironman', 'Kendall', 3)
    
    spiderman_movie = movie_repository.get_movie_by_title('Spiderman')
    avengers_movie = movie_repository.get_movie_by_title('Avengers')
    godzilla_movie = movie_repository.get_movie_by_title('Godzilla')
    ironman_movie = movie_repository.get_movie_by_title('Ironman')
    
    assert spiderman_movie == movie_repository.get_movie_by_id(spiderman_movie.movie_id)
    assert spiderman_movie != movie_repository.get_movie_by_id(avengers_movie.movie_id)
    
    assert avengers_movie == movie_repository.get_movie_by_id(avengers_movie.movie_id)
    assert avengers_movie != movie_repository.get_movie_by_id(godzilla_movie.movie_id)
    
    assert ironman_movie.movie_id == movie_repository.get_movie_by_title('Ironman').movie_id
    assert movie_repository.get_movie_by_id(ironman_movie.movie_id).movie_id == movie_repository.get_movie_by_title('Ironman').movie_id
    assert movie_repository.get_movie_by_id(ironman_movie.movie_id).movie_id != movie_repository.get_movie_by_title('Godzilla').movie_id
