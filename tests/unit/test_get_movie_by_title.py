from app import app
from src.repositories.movie_repository import get_movie_repository

def test_search_movies():
    #test user
    client = app.test_client()

    #  movie repository
    movie_repository = get_movie_repository()

    #  test movie
    test_movie = movie_repository.create_movie("Test Movie", "Test Director", 3)

    # this is the get request to search for the movie
    response = client.get('/movies/search', query_string={'query': 'Test Movie'})

    # Checks if the code equals 200 which indicates that the HTTP request was successful 

    assert response.status_code == 200

    # These asserts checks to see if the responses are in fact the expected movie data(b is what is used to compare the data with the string)
    assert b'Test Movie' in response.data
    assert b'Test Director' in response.data
    assert b'3' in response.data

    # Checks for Movie, director and rating
