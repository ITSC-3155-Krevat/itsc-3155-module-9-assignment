# TODO: Feature 4
from app import app

def test_single_movie_edit():
    # Create test client
    with app.test_client() as client:
        #opening single movie page
        response = client.get('/movies/1')
        assert response.status_code == 200

        # clicking the "Edit" button
        edit_link = f"/movies/1/edit"
        response = client.get(edit_link)
        assert response.status_code == 200
