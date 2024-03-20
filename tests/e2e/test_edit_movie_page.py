# TODO: Feature 5
from flask.testing import FlaskClient
from app import app
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_edit_page(test_app: FlaskClient):
    movie_repository.create_movie('Spiderman', 'Ronni Elhadidy', 5)
    movie = movie_repository.get_movie_by_title('Spiderman')
    movie_id = movie.movie_id

    response = test_app.get(f'/movies/{movie_id}/edit')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert f'<button type="submit" class="btn btn-primary">Update Movie</button>' in response_data