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
        'title': 'Titanic', 
        'director': 'James Cameron',
        'rating': '5'
    }, follow_redirects=True)

    assert response.status_code == 200
    #assert b"Titanic" in response.data
    assert b"5" in response.data

def test_movie_not_found(client):
    response = client.post('/movies/search', data = {
        'title':'2nd Test Movie',
        'director': '2nd Test Director',
        'rating': '4'}, follow_redirects=True)
    assert response.status_code == 200
    assert b"<h2>Movie Not Found.</h2>" not in response.data
    