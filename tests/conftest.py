from flask.testing import FlaskClient
from app import app
import pytest
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture(scope='module')
def test_app():
    return app.test_client()

# Loading movies into a test repository
@pytest.fixture(scope='module')
def preload_movies():
    repo = get_movie_repository()
    repo.create_movie('Call Me By Your Name', 'Luca Guadagnino', 5)
    repo.create_movie('Moonlight', 'Barry Jenkins', 5)