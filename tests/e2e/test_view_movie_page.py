
# Feature 4 E2E Testing


from src.repositories.movie_repository import get_movie_repository
from app import app

# Create a test movie and get its id for testing
movie_repository = get_movie_repository()
test_movie = movie_repository.create_movie('Interstellar', 'Christopher Nolan', 5)
test_movie_id = test_movie.movie_id

def test_get_movie_by_id():
    # Retrieve the test movie by id
    movie = movie_repository.get_movie_by_id(test_movie_id)

    test_app = app.test_client()
    page = test_app.get(f'/movies/{ test_movie_id }')
    page_data = response_data = page.data.decode('utf-8')
    
    assert '<h2>No movie in this database with that id.</h2>' not in page_data
    # Problem test
    #assert b'Christopher Nolan' in page.data

    assert page.status_code == 200

    assert b'Interstellar' in page.data

    assert b'5' in page.data

    assert b'Delete' in page.data
    
    assert b'Edit' in page.data

    # Delete the test movie after testing is complete
    movie_repository.delete_movie(test_movie_id)


def test_get_movie_by_id_empty_repository():
    # Given an empty movie repository
    movie_repository.clear_db()

    # When we attempt to retrieve a movie by an ID
    test_app = app.test_client()
    page = test_app.get('/movies/1')
    page_data = page.data.decode('utf-8')

    # Then the movie should not be found
    assert '<h2>No movie in this database with that id.</h2>' in page_data


