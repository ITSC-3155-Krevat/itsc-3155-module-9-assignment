# TODO: Feature 5
# first import the function we want to test via e2e test
from src.repositories.movie_repository import get_movie_repository
# import our app.py for e2e testing
from app import app
import conftest

# create our test function
def test_edit_e2e(test_app):
    response = test_app.get('/movies/<int:movie_id>')
    assert response.status_code == 200

# Resources
# https://www.youtube.com/watch?v=bToSg1TSpMA
