# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_get_movie_by_title():
    movie_repository = get_movie_repository()
    movie_repository.create_movie("Movie", "John Q", 1) #make sure that when a movie is created it has a title
    assert type(movie_repository.get_movie_by_title("Movie")) == Movie
    assert movie_repository.get_movie_by_title("Movie").title.__len__() > 0 #the movie title is longer than 0 to be a functional title
    assert movie_repository.get_movie_by_title("Movie").title == 'Movie' #the movie title that is created matches the title that is made
