def test_view_single_movie(test_app):
    response = test_app.get('/movies/1')
    assert response.status_code == 200
    assert b'Iron Man' in response.data  
    assert b'Jon Favreau' in response.data 
    assert b'5' in response.data 
