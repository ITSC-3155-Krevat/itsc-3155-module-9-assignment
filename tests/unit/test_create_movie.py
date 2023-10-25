# TODO: Feature 2 (Unit Test)
from src.repositories.movie_repository import get_movie_repository

def test_create_movie_unit():
    movie_repo = get_movie_repository()
    
    # clear db to make sure it starts out empty
    movie_repo.clear_db()
    
    # testing whether the movie repo is initially empty
    movies = movie_repo.get_all_movies()
    assert not movies
    
    # create new movie
    movie_name = "Random Movie"
    director = "Test Director"
    rating = 4
    
    # calling create_movie function to add movie to the repository
    movie = movie_repo.create_movie(movie_name, director, rating)
    
    # check if movie has been added to repository
    movies = movie_repo.get_all_movies()
    assert movie in movies.values() # check if created movie is in dictionary values
    