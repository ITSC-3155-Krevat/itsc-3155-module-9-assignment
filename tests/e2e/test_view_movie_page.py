#Anessa's get_single_movie test e2e feature
# Feature 4

import pytest
from app import app, movie_repository

@pytest.fixture(scope='module')
def client():
    with app.test_client() as client:
        yield client

def test_view_movie_page(client):
    movie_repository.clear_db()
    movie_id = 9999
    response = client.get(f'/movies/{movie_id}', data = {
        'movie_id': movie_id, 
        'title': 'Parasite', 
        'director': 'Bong Joon-ho', 
        'rating': 5
    }, follow_redirects=True)
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert '<h2 name="title">{{ movie.title }}</h2>' in response_data

def test_get_single_movie_without_id(client):
    movie_repository.clear_db()
    response = client.get('/get_single_movie', data={
        'title': 'Parasite',
        'director': 'Bong Joon-ho',
        'rating': 5
    }, follow_redirects=True)
    assert response.status_code == 404

def test_view_movie_page_validation_error(client):
    movie_repository.clear_db()
    movie_id = 9999
    response = client.get(f'/movies/{movie_id}')
    assert response.status_code != 404

def test_movie_id_not_found(client):
    movie_repository.clear_db()
    movie_id = 9999
    response = client.get(f'/movies/{movie_id}', data = {
        'title': 'Parasite',
        'director': 'Bong Joon-ho',
        'rating': 5
    }, follow_redirects=True)
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert '<h1>{{ error_status }} Error</h1>' not in response_data