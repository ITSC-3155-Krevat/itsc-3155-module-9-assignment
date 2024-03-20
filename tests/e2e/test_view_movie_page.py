#Anessa's get_single_movie test e2e feature
# Feature 4

import pytest
from app import app, movie_repository
from src.models.movie import Movie

@pytest.fixture(scope='module')
def client():
    with app.test_client() as client:
        yield client

def test_view_movie_page(client):
    movie_repository = Movie(9999, 'Parasite', 'Bong Joon-ho', 5)
    assert movie_repository.movie_id == 9999
    response = client.get(f'/movies/{movie_repository.movie_id}', data = {
        'title': movie_repository.title,
        'director': movie_repository.director,
        'rating': movie_repository.rating
    }, follow_redirects=True)
    response_data = response.data.decode('utf-8')
    if f'<h4>f"Movie with id: {movie_repository.movie_id} not found."</h4>' in response_data:
        assert '<h4>{{ error_message }}</h4>' in response_data
    else:
        assert response.status_code == 200
        assert f'<h4>f"Movie with id: {movie_repository.movie_id} not found."</h4>' not in response_data

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