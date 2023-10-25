# TODO: Feature 2
from app import app
from src.repositories.movie_repository import get_movie_repository

def test_create_movie():
    movie_repository = get_movie_repository() 
    movie_repository.create_movie(title='Test Movie', director='Test Director', rating=1)
    temp_dict = movie_repository.get_all_movies()
    #Tests to see if class is dict
    assert type(temp_dict) == type({})
    for key, value in temp_dict.items():
        assert value.title == 'Test Movie'
        assert value.director == 'Test Director'
        assert value.rating == 1
        assert 0<=key<=100_000
    
def test_create_movie_bad_data():
    movie_repository = get_movie_repository() 
    movie_repository.clear_db()
    movie_repository.create_movie(title='Bad Test', director='Not Director', rating=0)
    temp_dict = movie_repository.get_all_movies()
    #Tests to see if class is dict
    assert type(temp_dict) == type({})
    for key, value in temp_dict.items():
        assert value.title != 'Test Movie'
        assert value.director != 'Test Director'
        assert value.rating != 1
        assert 0<=key<=100_000

def test_create_movie_no_data():
    movie_repository = get_movie_repository() 
    movie_repository.clear_db()
    temp_dict = movie_repository.get_all_movies()
    #Tests to see if class is dict
    assert type(temp_dict) == type({})
    assert len(temp_dict.items()) == 0
        