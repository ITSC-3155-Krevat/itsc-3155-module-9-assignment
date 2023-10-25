# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository

def test_create_movie():
    get_movie_repository().create_movie('movie', 'director', 2)
    movie = get_movie_repository().get_all_movies()
    movie_id = list(movie.keys())[1]
    assert movie[movie_id].title == 'movie'
    assert movie[movie_id].director == 'director'
    assert movie[movie_id].rating == 2