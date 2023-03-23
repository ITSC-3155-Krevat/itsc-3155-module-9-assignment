# TODO: Feature 5
from app import app
from src.repositories.movie_repository import get_movie_repository

def test_update_movie():
   
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    movie = movie_repository.create_movie('Best Movie', 'Clayton', 5)

    movie = movie_repository.update_movie(movie.movie_id, 'New Title', 'New Director', 4)


    # Check that the movie was updated in the database
    assert movie.title == "New Title"
    assert movie.director == "New Director"
    assert movie.rating == 4

    movie_repository.clear_db()


