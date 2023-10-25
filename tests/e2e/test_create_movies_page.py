# TODO: Feature 2
from app import app
test_app = app.test_client()

def test_create_movie_page(test_app): 
    response = test_app.post('/movies', data={
        'rating': '5',
        'name': 'The Dark Knight',
        'director': 'Christopher Nolan'
    }, follow_redirects = True)

    data = response.data.decode()
    assert '<td>5</td>' in data
    assert '<td>The Dark Knight</td>' in data
    assert '<td>Christopher Nolan</td>' in data