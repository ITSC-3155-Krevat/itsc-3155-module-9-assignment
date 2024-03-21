# TODO: Feature 1

from src.models.movie import Movie
from app import app
from src.repositories.movie_repository import get_movie_repository

def test_list_all_movies_page(test_app):
    #test to see if the page is working

    response = test_app.get('/movies')
    assert response.status_code == 200
    assert response.status_code != 404

    response_data = response.data.decode('utf-8')

    assert b'<h1 class="mb-5">All Movies</h1>' in response.data
    assert b'<p class="mb-3">See our list of movie ratings below</p>' in response.data
   

def test_list_all_movies_working_table(test_app):
    #test to see if the table is working and displaying the movies
    movie_repository = get_movie_repository()
    movie_repository.clear_db()

    movie_repository.create_movie('The Shawshank Redemption', 'Frank Darabont', 9.2)
    movie_repository.create_movie('The Godfather', 'Francis Ford Coppola', 9.1)

    response = test_app.get('/movies')

    #assert
    assert response.status_code == 200
    assert b'The Shawshank Redemption' in response.data
    assert b'The Godfather' in response.data
    assert b'Frank Darabont' in response.data
    assert b'Francis Ford Coppola' in response.data
    assert b'9.2' in response.data
    assert b'9.1' in response.data

   










