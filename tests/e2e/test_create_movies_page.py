# TODO: Feature 2
from app import app

def test_create_movie():
    test_app = app.test_client()

    response = test_app.post('/movies', data = {
        'name': 'Dilwale',
        'director': 'Rohhit Sheey',
        'ratings': '4.0'
    }, follow_redirects = True)

    assert response.status_code == 200
    # assert ''
    # app.__getattribute__()