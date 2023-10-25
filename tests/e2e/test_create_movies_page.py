# TODO: Feature 2
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

def tests_create_movie(test_app: FlaskClient):
    # ensuring page loads correctly
    response = test_app.get('/movies')
    assert response.status_code == 200

    # create a movie sending a post request with dictionary through the form
    response = test_app.post('/movies', data ={
        'movieName': 'Random Movie',
        'director': 'Random Director',
        'rating': '4'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    
    assert b'Random Movie' in response.data
    assert b'Random Director' in response.data
    assert b'4' in response.data
    
    # make sure something got added to movie_repository
    movie_repo = get_movie_repository() 
    movies = movie_repo.get_all_movies().values()
    assert len(movies) == 1
    for movie in movies: 
        assert movie.title == 'Random Movie'