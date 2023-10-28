# TODO: Feature 1

from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository


def test_occupied_list(test_app: FlaskClient):
    movie_list = [
        {
            "title": "Aliens",
            "director": "James Cameron",
            "rating": "5"
            
        }, 
        {
            "title": "Suicide Squad", 
            "director": "David Ayer",
            "rating": "3"
        },
        {
            "title": "A Quiet Place",
            "director": "John Krasinski",
            "rating": "4"
        },
        {
            "title": "Pitch Perfect",
            "director": "Jason Moore",
            "rating": "2"
        }
    ]

    movie_repo = get_movie_repository()

    for movie_data in movie_list:
        movie_repo.create_movie(movie_data["title"], movie_data["director"], int(movie_data["rating"]))
        
    response = test_app.get('/movies')

    for movie_data in movie_list:
        for key, value in movie_data.items():
            assert str(value).encode() in response.data


def test_empty_list(test_app: FlaskClient):
    movie_repo = get_movie_repository()
    movie_repo.clear_db()

    response = test_app.get('/movies')

    assert b"There are currently no movie ratings." in response.data

