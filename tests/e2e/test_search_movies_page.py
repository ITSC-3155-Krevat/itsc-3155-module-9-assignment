# TODO: Feature 3
#varsha's end to end testing for search movies function
from flask.testing import FlaskClient
import pytest
from app import app

def test_search_movies_page(client: FlaskClient):
    response = client.get('/movies/search')
    assert response.status_code == 200
    assert b"Search Movie Ratings" in response.data

def test_search_movies_with_movie(client: FlaskClient):
    response = client.post('/movies/search', data = {
        'title': 'test title', 
        'director': 'test director',
        'rating': '5'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"test title" in response.data
    assert b"5" in response.data

def test_search_movies_without_movie(client: FlaskClient):
    response = client.post('/movies/search', data = {
        'title': 'test2 title', 
        'director': 'test2 director',
        'rating': '3'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"test3" not in response.data
    assert b"<h2>Movie Not Found.</h2>" in response.data