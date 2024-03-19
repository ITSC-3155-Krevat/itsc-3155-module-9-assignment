# TODO: Feature 1

from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie
from app import app

#Add the movie to the database and then check if it is there
def test_get_all_movies():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    movie_repository.create_movie('The Shawshank Redemption', 'Frank Darabont', 9.2)
    movie_repository.create_movie('The Godfather', 'Francis Ford Coppola', 9.1)

    movies = movie_repository.get_all_movies()

    #assert
    #checking if the 'movies' variale is a dictionary. As the get_all_movies() function returns a dictionary.
    assert isinstance(movies, dict)
    #checking if the length of the dictionary is 2. As we added 2 movies to the database
    assert len(movies) == 2

#check if the database is empty
def test_empty_db():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    movies = movie_repository.get_all_movies()
    
    #assert
    assert movie_repository.get_all_movies() == {}
    assert len(movies) == 0






   