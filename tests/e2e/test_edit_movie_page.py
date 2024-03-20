# TODO: Feature 5
from flask.testing import FlaskClient
from src.models.movie import Movie



def test_edit_page(test_app: FlaskClient):
    movie = Movie(123, 'Star Wars', 'George Lucas', 5)
    response = test_app.get(f"/movies/{movie.movie_id}/edit")  
    response_data = response.data.decode('utf-8')
    assert '<h1 class="mb-5">Edit Movie</h1>' in response_data
    assert type(movie) == Movie
