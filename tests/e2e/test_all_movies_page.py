# TODO: Feature 1
import pytest
from flask.testing import FlaskClient
from app import app
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_list_all_movies_page(client: FlaskClient):
    #test to see if the page is working

    response = client.get('/movies')
    response_data = response.data.decode('utf-8')

    #assert
    assert response.status_code == 200
    assert response.status_code != 404

    assert b'<h1 class="mb-5">All Movies</h1>' in response.data
    assert b'<p class="mb-3">See our list of movie ratings below</p>' in response.data

def test_list_all_movies_working_table(client: FlaskClient):
    #test to see if the table is working and displaying the movies

    movie_repository = get_movie_repository()
    movie_repository.clear_db()


    movie_repository.create_movie('The Shawshank Redemption', 'Frank Darabont', 9.2)
    movie_repository.create_movie('The Godfather', 'Francis Ford Coppola', 9.1)

    response = client.get('/movies')

    #assert
    assert response.status_code == 200
    
    assert b'The Shawshank Redemption' in response.data
    assert b'The Godfather' in response.data
    assert b'Frank Darabont' in response.data
    assert b'Francis Ford Coppola' in response.data
    assert b'9.2' in response.data
    assert b'9.1' in response.data







