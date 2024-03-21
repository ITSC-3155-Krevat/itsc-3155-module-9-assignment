#varsha's end to end testing for search movies function
from flask.testing import FlaskClient
from app import app

def test_search_movies_page():
    with app.test_client() as client:
        response = client.get('/movies/search')
        assert response.status_code == 200
        assert b"Search Movie Ratings" in response.data

def test_search_movies_with_movie():
    with app.test_client() as client:
        response = client.post('/movies/search', data = {
        'title': 'new', 
        'director': 'test director',
        'rating': '5'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"new" in response.data
    assert b"5" in response.data

def test_search_movies_without_movie():
    with app.test_client() as client:
        response = client.post('/movies/search', data = {
        'title': 'test2 title', 
        'director': 'test2 director',
        'rating': '3'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"test3" not in response.data
    assert b"<h3>Movie Not Found</h3>" in response.data