# TODO: Feature 2
from flask.testing import FlaskClient

def test_post_movie(test_app: FlaskClient) -> None: 
    response = test_app.post('/movies', data={
        'rating': '2',
        'name': 'iron man',
        'director': 'zane'
    }, follow_redirects = True)

    data = response.data.decode()
    
    assert '<td>2' in data 
    assert '<td> iron man' in data
    assert '<td> zane' in data
    assert response.status_code == 302

def test_post_movie_bad_information(test_app: FlaskClient) -> None:
    response = test_app.post('/movies', data={
        'rating': '2',
        'name': 'iron man',
        'director': ''
    }, follow_redirects = True)

    assert response.status_code == 400

    response = test_app.post('/movies', data={
        'rating': None,
        'name': 'iron man',
        'director': 'zane'
    }, follow_redirects = True)

    assert response.status_code == 400

    response = test_app.post('/movies', data={
        'rating': '3',
        'name': '',
        'director': 'zane'
    }, follow_redirects = True)

    assert response.status_code == 400

