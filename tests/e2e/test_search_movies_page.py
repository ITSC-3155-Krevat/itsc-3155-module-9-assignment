from app import app
from src.repositories.movie_repository import get_movie_repository
# TODO: Feature 3

def test_search():
    test_app = app.test_client()
    response = test_app.get('/movies/search')
    data = response.data.decode('utf-8')
    ##Test that page is rendered
    assert response.status_code == 200
    response = test_app.get('/movies/search?form_search=Pulp+Fiction')
    ##Test that page shows no movie is movie is not there
    assert b'<p class="mb-3">Movie not found.</p>' in response.data
    movie_repository = get_movie_repository()
    movie_repository.create_movie('The Matrix', 'The Wachowski Brothers', 5)
    response = test_app.get('/movies/search?form_search=The+Matrix')
    #ensures table is generatated if movie is found that shows the searched movie while also showing the full movie and rating and director
    assert b'<td>The Matrix</td>' in response.data
    assert b'<td>The Wachowski Brothers</td>' in response.data
    assert b'<td>5</td>' in response.data