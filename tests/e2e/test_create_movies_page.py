# TODO: Feature 2
from app import app
from src.repositories.movie_repository import get_movie_repository
import json

def test_create_movie():
    test_app = app.test_client()

    response = test_app.post('/movies', data={
        "movieName": "avengers",
        "directorName": "bob",
        "selectRating": 2
    })
    assert response.status_code == 302
    movie = get_movie_repository().get_movie_by_title('avengers')
    assert movie.title == 'avengers'
    assert movie.director == 'bob'
    assert movie.rating == 2

    response = test_app.get('/movies')
    assert b'<td>avengers</td>' in response.data
    assert b'<td>bob</td>' in response.data
    assert b'<td>2</td>' in response.data
