# TODO: Feature 1
from myapp import create_app
import pytest
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Setup: Clear the database and add mock entries if necessary
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    # Assuming you have a method to add movies for testing
    movie_repository.add_movie({'title': 'Test Movie', 'director': 'Test Director', 'rating': 5})
    
    yield  # this is where the testing happens

    # Teardown: Clear the database after tests
    movie_repository.clear_db()

def test_all_movies_page(client):
    # Test if the /movies page renders correctly
    response = client.get('/movies')
    assert response.status_code == 200
    assert b'Test Movie' in response.data
    assert b'Test Director' in response.data
    assert b'5' in response.data  # Check if the rating is in the response
