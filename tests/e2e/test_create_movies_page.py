# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository
from app import app, movie_repository
import pytest
from src.models.movie import Movie

@pytest.fixture()
def test_app():
  return app.test_client()

def test_movie_created_end(test_app):
    response = test_app.post('/movies', data={
        "movie_title": "Happy New Year",
        "director_name": "Karan Johar",
        "movie_rating": 4
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Happy New Year" in response.data
    assert b"Karan Johar" in response.data
    assert b"4" in response.data

    test_movie = Movie("Happy New Year", "Karan Johar", 5)
    all_movies = movie_repository.get_all_movies()
    print(test_movie.dict)

    same= False

    for movie in all_movies:
        if movie.dict == test_movie.dict:
            same = True

    assert same