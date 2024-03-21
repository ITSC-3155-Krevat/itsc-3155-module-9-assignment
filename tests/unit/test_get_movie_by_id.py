#Anessa's get_single_movie test unit feature
# Feature 4

import pytest
from flask import redirect
from app import app, movie_repository
from src.models.movie import Movie

def test_get_movie():
    added_movie = movie_repository.create_movie('Star Wars', 'George Lucas', 5)
    movies = movie_repository.get_all_movies()
    for movie in movies:
        if added_movie == movie:
            assert added_movie == movie
    assert added_movie != movie

def test_movie_id_validation_error():
    movie_id = 9999
    response = movie_repository.get_movie_by_id(movie_id)
    assert response == None
