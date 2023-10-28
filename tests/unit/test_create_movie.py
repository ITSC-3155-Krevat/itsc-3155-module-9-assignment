# TODO: Feature 2
from app import app
test_app = app.test_client()

def test_post_movie(): 
    response = test_app.post('/movies', data={
        'rating': '2',
        'name': 'iron man',
        'director': 'zane'
    }, follow_redirects = True)

    assert response.status_code == 200

def test_post_movie_bad_information():
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

