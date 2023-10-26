# TODO: Feature 4
from flask import Flask, app
from flask.testing import FlaskClient
import pytest
from app import app
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture()
def test_app():
    return app.test_client()

repo = get_movie_repository()

def test_find_id(test_app):
    movie = repo.create_movie("The Room", "Tommy", 5)
    id = movie.movie_id
    response = test_app.get('/movies/' + str(id))
    assert response.status_code == 200

def test_not_found_id(test_app):
    response = test_app.get('/movies/0')
    assert response.status_code == 400