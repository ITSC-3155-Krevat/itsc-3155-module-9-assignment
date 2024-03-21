# TODO: Feature 3


# this will test the case for when a movie exists in the database
def test_movie_title_found(test_app):
    # this sends a GET request to the search route with a query parameter for a movie title that exsists
    response = test_app.get('/movies/search?title=Test Movie')
    # Asserts that the HTTP response status code is 200 (success)
    assert response.status_code == 200
    # Asserts that the response data contains the bytes string "Test Movie" = e movie was found
    assert b"Test Movie" in response.data  


# this tests the case for when a movie does not exist in the database
def test_movie_title_not_found(test_app):
    response = test_app.get('/movies/search?title=Non-Existent Movie')
    assert response.status_code == 200
    assert b"No movie found with this title." in response.data

# this is test case for when no query is provided in the search
def test_movie_no_query(test_app):
    response = test_app.get('/movies/search')
    assert response.status_code == 200
    assert b"No movie found with this title." not in response.data
