# TODO: Feature 1
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository


def test_get_all_movies():
    movie_repository = get_movie_repository()
    movie_repository.create_movie('Toy Story', 'John Lasster', 3)
    
    movies = movie_repository.get_all_movies() 
    #converts the dict into a list and calls for the first index and assigns it to movie_id
    movie_id = list(movies.keys())[0] 
    #gets movie's key value and assigns it to toy_story_movie
    toy_story_movie = movies.get(movie_id)

    assert toy_story_movie.movie_id == movie_id
    assert toy_story_movie.title == 'Toy Story'
    assert toy_story_movie.director == 'John Lasster'
    assert toy_story_movie.rating == 3
    
def test_all_movies_rating():
    movie_repository = get_movie_repository()
    movie_repository.create_movie("Transformers", "Michael Bay", -1)
    movie_repository.create_movie("Transformers 2", "Michael Bay", 1)
    movie_repository.create_movie("Transformers 3", "Michael Bay", 3)
    movie_repository.create_movie("Transformers 4", "Michael Bay", 7)
    movies = movie_repository.get_all_movies()
    #this is to test the bonds of the rating for the movies
    for rate_movie in movie_repository.get_all_movies():
        x = 0
        movie_id = list(movies.keys())[x]
        rate_movie = movies.get(movie_id)
        assert rate_movie.rating >= 1
        assert rate_movie.rating <= 5
        x =+ 1