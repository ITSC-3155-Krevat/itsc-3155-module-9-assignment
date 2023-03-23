# TODO: Feature 2
from app import app

def test_create_movie(test_app):

    response = test_app.post('/movies', data={
        'mname': 'Jim',
        'dir': 'MyMovie',
        'rating': "3"
    }, follow_redirects=True)

    assert response.status_code == 200
    response = test_app.get("/movies")
    data = response.data.decode('utf-8')
    print (data)
    assert 'Jim' in data 
    assert 'Mymovie' in data 
    assert "3" in data

    response = test_app.post('/movies', data={
    'dir': 'Bob',
    'mname': 'Mymovie1',
    'rating': "6"
    }, follow_redirects=True)
    assert response.status_code == 200

    response = test_app.get("/movies") 
    data = response.data.decode('utf-8')
    assert not('Jim' in data and 'MyMovie1' in data and "6" in data)

    response = test_app.post('/movies', data={
    'dir': '',
    'mname': 'Mymovie2',
    'rating': "5"
    }, follow_redirects=True)

    assert response.status_code == 200
    response = test_app.get("/movies")
    data = response.data.decode('utf-8')

    assert not( 'Mymovie2' in data and "5" in data)

    response = test_app.post('/movies', data={
    'dir': 'John',
    'mname': '',
    'rating': "1"
    }, follow_redirects=True)
    
    assert response.status_code == 200
    response = test_app.get("/movies")
    data = response.data.decode('utf-8')

    assert not( 'John' in data and "1" in data)