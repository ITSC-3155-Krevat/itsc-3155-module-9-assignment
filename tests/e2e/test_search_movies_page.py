# TODO: Feature 3
from app import app

def test_search_movies_page(test_app):
    response = test_app.get('/movies/search', data={
    'title': '',
    'movie': 'Hello'
    }, follow_redirects=True)
    assert response.status_code == 200
    response = test_app.get("/movies/search") 
    data = response.data.decode('utf-8')
    assert not('' in data) #only thing that is important to search by title is that there exists a movie that has a title which has to be greater than 0