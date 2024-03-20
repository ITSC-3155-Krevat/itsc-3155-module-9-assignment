# TODO: Feature 4
from flask.testing import FlaskClient
from app import app
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_view_movie_end_to_end(test_app: FlaskClient):
    movie_repository.create_movie('Spiderman', 'Landon Nalewja', 5)
    movie = movie_repository.get_movie_by_title('Spiderman')
    movie_id = movie.movie_id

    response = test_app.get(f'/movies/{movie_id}')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert f'<h1 class="mb-5">{movie.title}</h1>' in response_data
    assert f'<h3>{movie.rating} Stars</h3>' in response_data
    assert f'<p>{movie.director}</p>' in response_data
    assert f'<form action="/movies/{movie_id}/edit" method="get">' in response_data
    assert f'<button type="submit">Delete</button>' in response_data
    assert f'<form action="/movies/{movie_id}/delete" method="post">' in response_data
    assert '<button type="submit">Edit</button>' in response_data