# TODO: Feature 5
import pytest
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository


@pytest.fixture
def movie_repo():
    # Clear the in-memory database before each test
    movie_repo = get_movie_repository()
    movie_repo.clear_db()
    return movie_repo


def test_update_model(movie_repo):
    # Create a new movie
    movie = movie_repo.create_movie("The Godfather", "Francis Ford Coppola", 5)
    
    #Assertions for the movie
    assert movie.title == "The Godfather"
    assert movie.director == "Francis Ford Coppola"
    assert movie.rating == 5
    
    #Updating the movie
    updated_movie = movie_repo.update_movie(movie.movie_id, "The Godfather: Part II", "Francis Ford Coppola", 4)
     
    # Check that the updated movie has the expected properties
    assert updated_movie.title == "The Godfather: Part II"
    assert updated_movie.director == "Francis Ford Coppola"
    assert updated_movie.rating == 4
        