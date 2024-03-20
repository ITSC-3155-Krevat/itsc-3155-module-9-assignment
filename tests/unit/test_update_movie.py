# TODO: Feature 5
import pytest
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture
def movie_repo():
    
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    return movie_repository

def test_update_movie(movie_repo):
    
    original_movie = movie_repo.create_movie("Test Movie", "Test Director", 3)

    updated_movie = movie_repo.update_movie(original_movie.movie_id, "Updated Movie", "Updated Director", 5)

  
    assert updated_movie.title == "Updated Movie"
    assert updated_movie.director == "Updated Director"
    assert updated_movie.rating == 5

