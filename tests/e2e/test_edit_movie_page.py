# TODO: Feature 5
# first import the function we want to test via e2e test
from src.repositories.movie_repository import get_movie_repository
# import our app.py for e2e testing
from app import app

# create our test for posting a movie update


def test_update_e2e(test_app):
    response = test_app.post('/movies/{{movie.movie_id}}', data={
        'title': 'FormerTrans',
        'director': 'Prime',
        'rating': 5
    }, follow_redirects=True)
    assert response.status_code == 404
    data = response.data.decode('utf-8')
   # assert 'FormerTrans' in data

# create our test for validation errors


def test_create_movie_validation_error(test_app):
    response = test_app.post('/movies/{{movie.movie_id}}')
    assert response.status_code == 404


# Resources
# https://www.youtube.com/watch?v=bToSg1TSpMA
