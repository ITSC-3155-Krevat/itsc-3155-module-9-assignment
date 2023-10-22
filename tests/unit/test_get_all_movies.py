from app import app
from src.repositories.movie_repository import get_movie_repository

# TODO: Feature 1 [DONE]
def test_get_all_movies():
    # test the app.py list_all_movies function
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    movies = movie_repository.get_all_movies()
    assert len(movie_repository.get_all_movies()) == 0
    movie_repository.create_movie('Sample movie', 'Bob Sample', 1)
    assert len(movie_repository.get_all_movies()) == 1
    movies = movie_repository.get_all_movies()
    for movie in movie_repository.get_all_movies():
        assert movies[movie].title == 'Sample movie'
        assert movies[movie].director == 'Bob Sample'
        assert movies[movie].rating == 1