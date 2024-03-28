# TODO: Feature 1

def test_list_all_movies(test_app):
    # Simulate accessing the /movies endpoint
    response = test_app.get('/movies')
    
    # Check if the response status code is 200 OK
    assert response.status_code == 200
    
    # Check if the expected heading is present
    assert '<h1 class="mb-5">All Movies</h1>' in response.text
    
    # Check if the expected table headers are present
    assert '<th scope="col">Movie Title</th>' in response.text
    assert '<th scope="col">Director</th>' in response.text
    assert '<th scope="col">Rating</th>' in response.text
    assert '<th scope="col">Actions</th>' in response.text
    
    # Check if the expected movie data is present
    assert '<td>Movie 1</td>' in response.text
    assert '<td>Director 1</td>' in response.text
    assert '<td>5</td>' in response.text
    assert '<td><a href="/movies/1/edit" class="btn btn-secondary btn-sm">Edit</a>' in response.text
    assert '<button type="submit" class="btn btn-danger btn-sm">Delete</button>' in response.text
    
    # You can add more assertions to check for additional movie data if needed
