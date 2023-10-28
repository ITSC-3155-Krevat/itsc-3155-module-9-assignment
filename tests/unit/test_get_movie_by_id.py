# TODO: Feature 4
from app import app
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_id():
    repo = get_movie_repository()
    
    movie1 = Movie(1, 'Golmal', 'Rohit Shetty', 5)
    movie2 = Movie(2, 'Bhagam bhag', 'Priyadarshan', 4)
    
    repo._db = {1: movie1, 2: movie2}
    
    movie = repo.get_movie_by_id(1)
    assert movie == movie1
    
    movie = repo.get_movie_by_id(2)
    assert movie == movie2
    
    movie = repo.get_movie_by_id(3)
    assert movie is None 
    
def test_delete_movie_by_id():
    repo = get_movie_repository()

    movie1 = Movie(1, 'Movie1', 'Director1', 5)
    repo._db = {1: movie1}

    success = repo.delete_movie(1)
    assert success is not None

    movie = repo.get_movie_by_id(1)
    assert movie is None 
    
    