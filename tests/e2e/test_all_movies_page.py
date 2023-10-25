# TODO: Feature 1
from app import app
from src.repositories.movie_repository import get_movie_repository

#check to see no table if no saved movies
def test_no_movies():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    
    test_client = app.test_client()
    response = test_client.post('/movies', data={}, follow_redirects=True)
    
    assert b'<h1 class="text-center">No Saved Movies!</h1>'

def test_one_movie():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    test_client = app.test_client()
    response = test_client.post('/movies', data={
        'title': 'Spiderman',
        'director': 'Zaid Jebril',
        'rating': 3
    }, follow_redirects=True)

    # asserting that movie is posted correctly and non existent movie isnt there
    assert response.status_code == 200
    assert b'<td>Spiderman</td>' in response.data
    assert b'<td>Zaid Jebril</td>' in response.data
    assert b'<td>3</td>' in response.data
    assert b'<td>Batman</td>' not in response.data

    response = test_client.post('/movies', data={
        'title': 'Batman',
        'director': 'Sam Smith',
        'rating': 2
    }, follow_redirects=True)

    # asserting that first movie posted is still there after movie is added and new movie is there as well
    assert response.status_code == 200
    assert b'<td>Spiderman</td>' in response.data
    assert b'<td>Batman</td>' in response.data
    assert b'<td>2</td>' in response.data

    movie_repository.clear_db()

