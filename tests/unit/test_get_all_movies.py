# Jaidens Unit testing for the List all movies function

from src.repositories.movie_repository import get_movie_repository
from app import list_all_movies

movie_repository = get_movie_repository()

def test_movies_list_empty_size():
    movie_repository.clear_db()
    movies = []
    assert len(movies) == 0
    movie_repository.clear_db()


def test_movies_list_not_empty_size():
    movie_repository.clear_db()
    movies = []
    movie1 = movie_repository.create_movie("Up", "Director", 4)
    movies.append(movie1)
    moviesLength = len(movies)
    assert moviesLength == 1
    movie_repository.clear_db()

def test_movies_list_not_empty():
    movie_repository.clear_db()
    movies = []
    movie1 = movie_repository.create_movie("Up", "Director", 4)
    movie2 = movie_repository.create_movie("Toy Story", "Director", 4)
    moviesList = movie_repository.get_all_movies()
    for i in moviesList:
        movie = movie_repository.get_movie_by_id(i)
        movies.append(movie)
    assert movies[0] == movie1
    assert movies[1] == movie2
    movie_repository.clear_db()
