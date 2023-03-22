# TODO: Feature 2
from app import app

def test_create_movie(test_app):

    # response = test_app.post('/movies', data={
    #     'dir_name': 'Jim',
    #     'movie_name': 'MyMovie',
    #     'rating': "3"
    # }, follow_redirects=True)

    # assert response.status_code == 200
    # response = test_app.get("/movies")
    # data = response.data.decode('utf-8')

    # assert 'Jim' in data and 'MyMovie' in data and "3" in data

    response = test_app.post('/movies', data={
    'dir_name': 'Bob',
    'movie_name': 'MyMovie1',
    'rating': "6"
    }, follow_redirects=True)
    assert response.status_code == 200

    response = test_app.get("/movies") 
    data = response.data.decode('utf-8')
    assert not('Jim' in data and 'MyMovie1' in data and "6" in data)

    response = test_app.post('/movies', data={
    'dir_name': '',
    'movie_name': 'MyMovie2',
    'rating': "5"
    }, follow_redirects=True)

    assert response.status_code == 200
    response = test_app.get("/movies")
    data = response.data.decode('utf-8')

    assert not( 'MyMovie2' in data and "5" in data)

    response = test_app.post('/movies', data={
    'dir_name': 'John',
    'movie_name': '',
    'rating': "1"
    }, follow_redirects=True)

    assert response.status_code == 200
    response = test_app.get("/movies")
    data = response.data.decode('utf-8')

    assert not( 'John' in data and "1" in data)