# TODO: Feature 3
from app import app

def test_search_movies_page(test_app):
    response = test_app.post('/movies/search')
    title = 'Hello'
    data = response.data.decode('utf-8')
    assert  'Hello' in data