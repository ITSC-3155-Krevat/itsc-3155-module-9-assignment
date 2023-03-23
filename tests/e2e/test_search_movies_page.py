# TODO: Feature 3
from app import app
from src.repositories.movie_repository import MovieRepository

client = app.test_client()
movie_repository = MovieRepository()


def test_search_movies_page():

    movie_repository.create_movie("The Dark Knight", "Christopher Nolan", 5)
    movie_repository.create_movie("Inception", "Christopher Nolan", 4)
    movie_repository.create_movie("The Matrix", "Lana Wachowski and Lilly Wachowski", 4)
    
    response = client.get('/movies/search')
    
    assert response.status_code == 200
    
    assert b'<form method="get" action="/movies/search/results">' in response.data
    
    assert b'<button type="submit" class="btn btn-primary">Search</button>' in response.data
