# TODO: Feature 4
from app import get_single_movie
from app import app
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository



def test_get_single_movie():
    movie = get_movie_repository()
    
    test_movie = movie.create_movie(title='test',director='john', rating=5)
    
    movie_info = movie.get_movie_by_id(test_movie.movie_id)

    assert movie_info.movie_id == test_movie.movie_id
    assert movie_info.title == 'test'
    assert movie_info.director == 'john'
    assert movie_info.rating == 5
