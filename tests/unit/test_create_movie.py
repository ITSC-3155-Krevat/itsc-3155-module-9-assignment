# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_create_movie():
    movie_repository = get_movie_repository()
    movie_repository.create_movie("Movie", "Jim Bob", 4)
    my_id = movie_repository.get_movie_by_title("Movie").movie_id
    assert type(movie_repository.get_movie_by_title("Movie")) == Movie
    assert movie_repository.get_movie_by_title("Movie").movie_id <= 100000
    assert movie_repository.get_movie_by_title("Movie").movie_id >= 0
    assert movie_repository.get_movie_by_title("Movie").title == 'Movie'
    assert movie_repository.get_movie_by_title("Movie").director == 'Jim Bob'
    assert movie_repository.get_movie_by_title("Movie").rating == 4
    assert movie_repository.get_movie_by_id(my_id).title == 'Movie'
    
    
