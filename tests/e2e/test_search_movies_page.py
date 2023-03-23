# TODO: Feature 3
from app import app

def test_search_movies_page(test_app):
    response = test_app.post('/movies/search', data={'title': 'Hello'}, follow_redirects=True)
    response = test_app.get('/movies/search')
    data = response.data.decode('utf-8')
    assert  'title' in data

    response = test_app.post('/movies/search', data={'title': 'Tarzan'}, follow_redirects=True)
    response = test_app.get('/movies/search')
    data = response.data.decode('utf-8')
    assert not('Hello' in data)

    response = test_app.post('/movies/search', data={'title': ''}, follow_redirects=True)
    response = test_app.get('/movies/search')
    data = response.data.decode('utf-8')
    assert '' in data