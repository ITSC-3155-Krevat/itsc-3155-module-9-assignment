# TODO: Feature 5
# TODO: Feature 5
import pytest
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository
from flask.testing import FlaskClient


def test_edit_page(test_app: FlaskClient):
    response = test_app.get('/movies/1/edit')
    response_data = response.data.decode('utf-8')

    assert '<h1 class="mb-5">Edit Movie</h1>' in response_data
    assert response.status_code == 200

#def test_update_movie(test_app: FlaskClient):
   # movie_repo = get_movie_repository()
   # movie = movie_repo.get_movie_by_id(1)

    
   # response = test_app.post('/movies/1', data={
   #         'title': 'Title',
    #        'director': 'Director',
     #       'rating': '5'
      #  }, follow_redirects=True)
    
    # assert response.status_code == 200
    
    # data = response.data.decode('utf-8')
    
    # assert '<h1>Title: Title</h1>' in data
    
        