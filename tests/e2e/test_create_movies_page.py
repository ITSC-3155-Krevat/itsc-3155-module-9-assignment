# TODO: Feature 2
from app import app

def test_create_movie():
    client = app.test_client()

    response = client.post('/movies', data={
        'title': 'Test Movie',
        'director': 'Test Director',
        'rating': 1
    }, follow_redirects=True)

    data = response.data.decode()

    assert response.status_code == 200
    assert '<td>Test Movie</td>' in data
    assert '<td>Test Director</td>' in data 
    assert '<td>1</td>' in data
                    
def test_movie_bad_request():
    client = app.test_client()

    response = client.post('/movies', data={}, follow_redirects=True)

    data = response.data.decode()

    #Goes back to original (/movies/new) page, and doesn't go to table page(/movies) because data is empty
    assert response.status_code == 200
    assert '<label for="title" class="form-label">Title: </label>' in data

