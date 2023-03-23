# TODO: Feature 3

from src.repositories.movie_repository import get_movie_repository
from app import app

# Create a test movie and get its id for testing
movie_repository = get_movie_repository()
test_movie = movie_repository.create_movie('Interstellar', 'Christopher Nolan', 9)
movieTitle = test_movie.title

def test_search_movies():
    # Retrieve the test movie by id
    movie = movie_repository.get_movie_by_title(movieTitle)

    test_app = app.test_client()
    page = test_app.get(f'/movies/search?title={movie.title}')
    page_data = response_data = page.data.decode('utf-8')
    
    assert '<p>No rating found for' not in page_data
    # Problem test
    #assert b'Christopher Nolan' in page.data

    assert page.status_code == 200

    assert b'Interstellar' in page.data

    assert b'9' in page.data

    assert b'submit' in page.data
    
    assert b'/10' in page.data

    # Delete the test movie after testing is complete
    movie_repository.delete_movie(movie.title)


def test_get_movie_by_id_empty_repository():
    # Given an empty movie repository
    movie_repository.clear_db()

    # When we attempt to retrieve a movie by an ID
    test_app = app.test_client()
    page = test_app.get(f'/movies/search?title=hello')
    page_data = page.data.decode('utf-8')

    # Then the movie should not be found
    assert '<p>No rating found for' in page_data


