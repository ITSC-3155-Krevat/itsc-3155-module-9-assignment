# Feature 3
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_title():
    get_movie_repository().create_movie('Test Movie', 'Test Director', 3)
    movie = get_movie_repository().get_movie_by_title('Test Movie')
    assert movie.title == 'Test Movie'
    assert movie.director == 'Test Director'
    assert movie.rating == 3
