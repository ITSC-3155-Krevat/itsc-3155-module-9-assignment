
import pytest
from flask import url_for
from src.repositories.movie_repository import get_movie_repository




# Test viewing a single movie
@pytest.mark.parametrize('movie_id, expected_status_code', [
    (1, 200),  # Existing movie
    (9999, 404)  # Non-existing movie
])

def test_view_single_movie(client, movie_id, expected_status_code):
    response = client.get(url_for('view_single_movie', movie_id=movie_id))
    assert response.status_code == expected_status_code

# Test deleting a movie
@pytest.mark.parametrize('movie_id, expected_status_code', [
    (1, 204),  # Existing movie
    (9999, 404)  # Non-existing movie
])

def test_delete_movie(client, movie_id, expected_status_code):
    response = client.delete(url_for('delete_movie', movie_id=movie_id))
    assert response.status_code == expected_status_code
