# TODO: Feature 2
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository


def test_create_movie():
   movie_repository = get_movie_repository()
   title = 'Happy New Year'
   director = 'Karan Johar'
   rating = 4
   movie = movie_repository.create_movie(title, director, rating)

    
    
   assert movie.title == 'Happy New Year'
   assert movie.director == 'Karan Johar'
   assert movie.rating == 4