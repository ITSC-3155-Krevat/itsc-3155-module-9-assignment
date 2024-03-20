#Jaidens e2e testing for the List all movies function

from flask.testing import FlaskClient
from app import app, list_all_movies

from src.repositories.movie_repository import get_movie_repository
movie_repository = get_movie_repository()


def test_list_empty(test_app: FlaskClient):
    movie_repository.clear_db()
    response = test_app.get('/movies')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert '<h2>No Movies Available!</h2>' in response_data
    movie_repository.clear_db()

def test_list_not_empty(test_app: FlaskClient):
    movie_repository.clear_db()
    movie1 = movie_repository.create_movie("Up", "Director", 4)
    response = test_app.get('/movies')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert '''<table class="table table-striped table-dark">'''in response_data
    assert "<td>Up</td>" in response_data
    assert "<td>Director</td>" in response_data
    assert "<td>4</td>" in response_data
    movie_repository.clear_db()

