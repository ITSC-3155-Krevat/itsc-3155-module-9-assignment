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
    # data = response.data.decode()
    # print(data)
    # assert '<td>Dilwale</td>' in data
    # assert ''
    # app.__getattribute__()


def test_create_movie_2():
    test_app = app.test_client()

    response = test_app.post('/movies', data = {
        'name': 'Dilwale',
        'director': 'Rohhit Sheey',
        'ratings': '4.0'
    }, follow_redirects = True)
    data = response.data.decode()
    assert '<td>Dilwale</td>' in data

def test_no_input():
    test_app = app.test_client()

    response = test_app.post('/movies', data = {
        'name': '',
        'director': '',
        'ratings': ''
    }, follow_redirects = True)
    data = response.data.decode()
    assert response.status_code == 400
    
def test_invalid_rating_greater_than():
    test_app = app.test_client()

    response = test_app.post('/movies', data = {
        'name': 'Dilwale',
        'director': 'Rohit Shetty',
        'ratings': '5.5'
    }, follow_redirects = True)
    data = response.data.decode()
    assert response.status_code == 400

def test_invalid_rating_less_than():
    test_app = app.test_client()

    response = test_app.post('/movies', data = {
        'name': 'Dilwale',
        'director': 'Rohit Shetty',
        'ratings': '-0.5'
    }, follow_redirects = True)
    data = response.data.decode()
    assert response.status_code == 400