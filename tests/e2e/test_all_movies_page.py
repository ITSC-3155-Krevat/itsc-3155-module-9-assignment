# TODO: Feature 1

from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie 

#initializing a test repository
test_repository = get_movie_repository()

#initializing test movies
movie1 = test_repository.create_movie('First movie', 'Director 1', 1)
movie2 = test_repository.create_movie('Second movie', 'Director 2', 2)
movie3 = test_repository.create_movie('Third movie', 'Director 3', 3)

#testing movies added to page
def test_all_movies_page(test_app):
    response = test_app.get('/movies', data = {Movie})
    assert response.status_code == 200