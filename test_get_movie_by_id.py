# TODO: Feature 4
from app import app

def test_single_movie_page():
    with app.test_client() as client:
        # Simulate rendering the single movie page
        response = client.get('/movies/1')  # Assuming movie ID 1 for testing
        assert response.status_code == 200

        # Check if movie details are displayed
        assert b'<h1 class="mb-5">Movie Title</h1>' in response.data  
        assert b'<strong>ID:</strong> 1' in response.data  
        assert b'<strong>Director:</strong> Director Name' in response.data  
        assert b'<strong>Rating:</strong> 9.0' in response.data  

        # Check if "Edit" button is present
        assert b'<a href="/movies/1/edit" class="btn btn-primary">Edit</a>' in response.data
