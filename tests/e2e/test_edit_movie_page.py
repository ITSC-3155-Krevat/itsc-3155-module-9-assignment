# TODO: Feature 5
# TODO: Feature 5
import pytest
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository
from flask.testing import FlaskClient


def test_edit_page(test_app: FlaskClient):
    response = test_app.get('/movies/<int:movie_id>/edit')
    response_data = response.data.decode('utf-8')

    assert '<h1 class="mb-5">Edit Movie</h1>' in response_data
        