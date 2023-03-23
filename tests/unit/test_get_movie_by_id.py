# TODO: Feature 4
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def test_search_movies_page(test_app):
    response = test_app.post('/movies/search', data={'id': 1}, follow_redirects=True)
    response = test_app.get('/movies/search')
    data = response.data.decode('utf-8')
    assert  'id' in data


def test_get_single_movie_with_empty_id(client):

    empty_id = ""
    response = client.get(f'/movies/{empty_id}')
    assert response.status_code == 404