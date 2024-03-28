# TODO: Feature 1
# test_all_movies_page.py

from src.repositories.movie_repository import get_movie_repository
from app import app
from flask import url_for

def test_list_all_movies(client):
    # Create an instance of MovieRepository
    movie_repository_test = get_movie_repository()

    # Add some sample movies to the repository
    movie_repository_test.create_movie("The Shawshank Redemption", "Frank Darabont", 3.2)
    movie_repository_test.create_movie("The Godfather", "Francis Ford Coppola", 5.0)
    movie_repository_test.create_movie("The Dark Knight", "Christopher Nolan", 4.3)
    movie_repository_test.create_movie("Forrest Gump", "Robert Zemeckis", 4.5)

    # Test accessing the list all movies page
    response = client.get(url_for('list_all_movies'))

    assert response.status_code == 200

    # Check if movie titles are present in the response content
    assert b"The Shawshank Redemption" in response.data
    assert b"The Godfather" in response.data
    assert b"The Dark Knight" in response.data
    assert b"Forrest Gump" in response.data

    # Check if movie directors are present in the response content
    assert b"Frank Darabont" in response.data
    assert b"Francis Ford Coppola" in response.data
    assert b"Christopher Nolan" in response.data
    assert b"Robert Zemeckis" in response.data

    # Check if movie ratings are present in the response content
    assert b"3.2" in response.data
    assert b"5.0" in response.data
    assert b"4.3" in response.data
    assert b"4.5" in response.data

