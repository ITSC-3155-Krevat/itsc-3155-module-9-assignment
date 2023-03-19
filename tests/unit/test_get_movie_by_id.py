# TODO: Feature 4 As a user, I should be able to view a movie in isolation and have access to edit and delete that movie. There is no csv file for this feature.

from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_id(movie_repository):
    # Arrange: Insert a movie into the database
    movie = Movie(title='Test Movie', rating=5)
    movie_repository.insert_movie(movie)

    # Act: Retrieve the movie by ID using the get_movie_by_id function
    retrieved_movie = movie_repository.get_movie_by_id(movie.id)

    # Assert: Make sure the retrieved movie matches the original movie
    assert retrieved_movie.id == movie.id
    assert retrieved_movie.title == movie.title
    assert retrieved_movie.rating == movie.rating

    # Clean up: Delete the movie from the database
    movie_repository.delete_movie(movie.id)

