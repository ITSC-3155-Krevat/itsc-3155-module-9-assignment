from flask.testing import FlaskClient

def test_edit_movie_page_render(test_app: FlaskClient):
    
    response = test_app.get('/movies/1/edit')
    
    response_data = response.data.decode('utf-8')
    
    assert response.status_code == 200
    
    assert '<h1 class="mb-5">Edit Movie</h1>' in response_data
    assert 'Movie Name' in response_data
    assert 'Director' in response_data
    assert 'Rating' in response_data


