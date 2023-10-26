# TODO: Feature 3 
from app import app 
from src.models.movie import Movie 
from src.repositories.movie_repository import get_movie_repository 



def test_get_movie_by_title(): 
    movie = get_movie_repository() 
    mock_movie = movie.create_movie("test 1", "john", 4) 

    movie_info = movie.get_movie_by_title(mock_movie.title) 

    assert movie_info.title == "test 1"
    assert movie_info.rating == 4 

     


