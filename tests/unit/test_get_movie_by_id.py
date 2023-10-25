
import pytest
from src.repositories.movie_repository import get_movie_repository

# TODO: Feature 4

# Initialize mock data
mock_movie_data = {
    'id': 1,
    'title': 'Inception',
    'director': 'Christopher Nolan',
    'genre': 'Sci-Fi',
    'release_year': 2010
}

def test_get_movie_by_id():
    # Add mock data to repository
    movie_repository.add_movie(mock_movie_data)
    
    # Test get_movie_by_id method
    movie = movie_repository.get_movie_by_id(1)
    assert movie['id'] == 1
    assert movie['title'] == 'Inception'
    assert movie['director'] == 'Christopher Nolan'
    assert movie['genre'] == 'Sci-Fi'
    assert movie['release_year'] == 2010

def test_delete_movie_by_id():
    # Add mock data to repository
    movie_repository.add_movie(mock_movie_data)
    
    # Test delete_movie_by_id method
    success = movie_repository.delete_movie_by_id(1)
    assert success == True
    
    # Verify movie is deleted
    movie = movie_repository.get_movie_by_id(1)
    assert movie is None