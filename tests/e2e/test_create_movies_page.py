# TODO: Feature 2

# tests/e2e/test_create_movies_page.py -- Cindy's Save function 
from app import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_movie_duplicate(client):
    #add a movie 
    client.post('/movies/new', data={
        'title': 'Existing Movie',
        'director': 'Existing Director',
        'rating': '4'
    })

    #create a duplicit 
    response = client.post('/movies/new', data={
        'title': 'Existing Movie',
        'director': 'Existing Director',
        'rating': '5'
    }, follow_redirects=True)  

    assert response.status_code == 200

    assert b'Movie already exists' in response.data
