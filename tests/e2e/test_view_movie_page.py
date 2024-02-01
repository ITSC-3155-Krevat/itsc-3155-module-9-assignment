# TODO: Feature 4: As a user, I should be able to view a movie in isolation and have access to edit and delete that movie.

from app import app
from src.repositories.movie_repository import get_movie_repository

# TODO: Feature 4
def test_get_single_movie():
    # Set up
    test_app = app.test_client()
    movie_repo = get_movie_repository()

    # Create a test movie
    test_movie = movie_repo.create("Test Movie", 2022)

    # Test getting a single movie by its ID
    response = test_app.get(f"/movies/{test_movie.id}")
    assert response.status_code == 200

    # Check that the returned data matches the test movie
    data = response.json
    assert data["id"] == test_movie.id
    assert data["title"] == test_movie.title
    assert data["year"] == test_movie.year

    # Clean up
    movie_repo.delete(test_movie.id)
