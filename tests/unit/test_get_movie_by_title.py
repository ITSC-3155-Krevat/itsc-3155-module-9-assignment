# TODO: Feature 3
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_search_movies(client):
    response = client.get('/movies/search')
    assert response.status_code == 200
    assert b"Search Movie Ratings" in response.data

def test_search_movies_rating(client):
    response = client.post('/movies/search', data = {
        'title': 'test' 
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"test" in response.data

def test_movie_not_found(client):
    response = client.post('/movies/search', data = {
        'title':'2nd Test Movie'
        }, follow_redirects=True)
    assert response.status_code == 200
    assert b"<h3>Movie Not Found</h3>" in response.data
    