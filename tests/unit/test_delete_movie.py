# TODO: Feature 6
from app import app
from src.repositories.movie_repository import get_movie_repository

def test_delete_movie(movie_id: int):

    movie_repository = get_movie_repository()
    movie_repository.delete_movie = app(return_value=True)  # Mocking the delete_movie method
    
result = movie_repository.delete_movie(1)  # Assuming 1 is a valid movie ID
    
assert result is True

def test_delete_non_existing_movie():
    movie_repository = get_movie_repository()
    movie_repository.delete_movie = app(return_value=False)  # Mocking the delete_movie method
    
    result = movie_repository.delete_movie(999)  # Assuming 999 is a non-existing movie ID
    
    assert result is False