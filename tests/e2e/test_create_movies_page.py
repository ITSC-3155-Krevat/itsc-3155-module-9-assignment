from app import app
from src.repositories.movie_repository import get_movie_repository

# TODO: Feature 2 [DONE]
def test_create_movie_form():
    #Test no data is posted before submit button is pressed
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    tester = app.test_client()
    response = tester.get('/movies')
    assert response.status_code == 200
    assert b'<td colspan="3">No movies found</td>' in response.data

    #Test that input given is correctly placed in table
    response = tester.post(
      '/movies',
      data = dict(title="Avatar", director="James Cameron", rating="5", login_form="movie_form"),
      follow_redirects=True
      )
    assert response.status_code == 200
    assert b'<td>Avatar</td>' in response.data
    assert b'<td>James Cameron</td>' in response.data
    assert b'<td>5/5</td>' in response.data

    #Test that nothing happens if no data is submitted
    movie_repository.clear_db()
    response = tester.post(
      '/movies',
      data = dict(login_form="movie_form"),
      follow_redirects=True
      )
    assert response.status_code == 200
    assert b'<td colspan="3">No movies found</td>' in response.data

    #Clear database
    movie_repository.clear_db() 

    
    
# RESOURCES: 
# - https://stackoverflow.com/questions/32290830/how-to-unit-test-a-form-submission-when-multiple-forms-on-a-route

# NOTES:
# Search by request also possible? => queryString => movie-name=Avatar&director=James+Cameron&rating=5