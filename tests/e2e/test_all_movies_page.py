# TODO: Feature 1
from flask.testing import FlaskClient
from app import app
import pytest
from src.repositories.movie_repository import get_movie_repository

# Loading movies into a test repository
@pytest.fixture(scope='module')
def preload_movies():
    repo = get_movie_repository()
    repo.create_movie('Call Me By Your Name', 'Luca Guadagnino', 5)
    repo.create_movie('Moonlight', 'Barry Jenkins', 5)

def test_all_movies_page(test_app, preload_movies):
    # Getting response from test app for list_all_movies page
    response = test_app.get('/movies')

    # Verifying response code is '200 OK'
    assert response.status_code == 200

    # Verifying page content loaded
    assert b'<h1 class="mb-5">All Movies</h1>' in response.data

    # Verifying page content INCLUDING movie_repository data was loaded
    assert b'<td>Call Me By Your Name</td>' in response.data
    assert b'<td>Moonlight</td>' in response.data