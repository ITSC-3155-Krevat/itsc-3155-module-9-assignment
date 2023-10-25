# TODO: Feature 1
from flask.testing import FlaskClient

def test_create_movie(test_app: FlaskClient):
    # Send a GET request to the '/movies' route
    response = test_app.get('/movies')
    assert response.status_code == 200

    response = test_app.post('/movies', data = {
        'movieName': 'TestTitle',
        'director': 'TestDirector',
        'rating': '5'
    }, follow_redirects=True)
    assert response.status_code == 200

    assert b'TestTitle' in response.data
    assert b'TestDirector' in response.data
    assert b'5' in response.data