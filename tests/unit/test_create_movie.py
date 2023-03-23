# TODO: Feature 2
from app import create_movie

def test_create_movie():
    movie_repository = get_movie_repository()
    length = movie_repository.get_all_movies()

    movie_repository.create_movie('test','test',0)

    assert length != movie_repository.get_movie_repository.length
    

