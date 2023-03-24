# TODO: Feature 3
from app import app
from src.repositories.movie_repository import get_movie_repository

# creating a movie repository
temp_movie_repository = get_movie_repository()

# adding movies to the movie repository
temp_movie_repository.create_movie('Movie A', 'Director A', 1)
temp_movie_repository.create_movie('Movie B', 'Director B', 2)
temp_movie_repository.create_movie('Movie C', 'Director C', 3)
temp_movie_repository.create_movie('Movie D', 'Director D', 4)

def test_search_movies_page(test_app):

    # testing when the movie exist
    response = test_app.get('/movies/search', data={
        'movie-name': 'Movie A'
    })
    assert response.status_code == 200
    

    response = test_app.post('movies/search', data={
        'movie-name': 'Movie A'
    })
    assert response.status_code == 200

    # testing when the movie don't exist
    response = test_app.get('movies/search', data={
        'movie-name': 'Movie B'
    })
    assert response.status_code == 200
    data = response.data.decode('utf-8')
    assert '<p class="mb-3">Movie not found.</p>' in data

    


  



