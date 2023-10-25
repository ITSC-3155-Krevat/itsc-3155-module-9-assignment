# TODO: Feature 6
from app import app

def test_delete_movie_page(client):

    response = client.post('/movies/1/delete')  # Assuming 1 is a valid movie ID
    
    # Assert that the response status code is 302
    assert response.status_code == 302