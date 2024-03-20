import pytest
from app import app

# TODO: Feature 2
def test_create_movies_page(test_app):
    client = test_app
    
    response = client.post('/movies', data={'title': 'Test title', 'director': 'Director Test', 'rating': 3})
    
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/movies'
    
    assert b'Movie successfully created' in response.data
    assert b'Test title' in response.data
    assert b'Director Test' in response.data
    assert b'3' in response.data