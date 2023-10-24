from app import app
from src.repositories.movie_repository import get_movie_repository

# TODO: Feature 4
def test_get_single_movie():
    test_app = app.test_client()

    data = response.data.decode('utf-8')
    response =  test_app.get('/movies/search')
    assert response.status_code == 200
    

    ##Test that page is rendered
    
