# TODO: Feature 2

from app import app



def test_create_movie():
    test_app = app.test_client()
    
    response = test_app.get('/create_movie')
    
    assert response.status_code == 200
    assert <p class="mb-3">Create a movie rating below</p> in response.data

