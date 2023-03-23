# TODO: Feature 4
import pytest
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_id():
    m_repo = get_movie_repository()
    movie = m_repo.create_movie('Scarface', 'Brian De Palma', 4)
    all_movies = m_repo.get_all_movies()
    
    assert type(movie.movie_id) == int
    assert (movie.title) == 'Scarface'
    assert (movie.director) == 'Brian De Palma'
    assert (movie.rating) == 4
