from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_search_movies_end_to_end(test_app: FlaskClient):

    movie_repository.create_movie('Spiderman', 'Landon Nalewja', 5)
    movie_repository.create_movie('Harry Potter', 'JK Rowling', 9)

    response = test_app.get('/movies/search?query=Spiderman')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert '<h1 class="mb-5">Search Movie Ratings</h1>' in response_data

    response = test_app.get('/movies/search?query=Spiderman')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert '<label for="search_query">Enter Movie Title:</label>' in response_data

    another_response = test_app.get('/movies/search?query=Harry Potter')
    another_response_data = another_response.data.decode('utf-8')
    assert another_response.status_code == 200
    assert '<button type="submit">Search</button>' in another_response_data

    another_response = test_app.get('/movies/search?query=Harry Potter')
    another_response_data = another_response.data.decode('utf-8')
    assert another_response.status_code == 200
    assert '<input type="text" id="search_query" name="query" required>' in another_response_data

