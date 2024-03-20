# TODO: Feature 1
from flask.testing import FlaskClient
from app import movie_repository

def test_all_movies_page(test_app: FlaskClient):
    response = test_app.get('/movies')
    data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert '<p class="mb-3">Our list of movie is empty :(</p>' in data

    test_app.post('/movies', data = {
        'title': 'The Matrix',
        'director': 'The Wachowskis',
        'rating': 5,
    })
    response = test_app.get('/movies')
    data = response.data.decode('utf-8')
    id = list(movie_repository.get_all_movies())[0]

    assert response.status_code == 200
    assert '<p class="mb-3">Our list of movie is empty :(</p>' not in data
    assert f'<td scope="row">{id}</td>' in data
    assert '<td>The Matrix</td>' in data
    assert '<td>The Wachowskis</td>' in data
    assert '<td>5</td>' in data

    movie_repository.clear_db()