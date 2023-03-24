# TODO: Feature 2

#Create a movie and verify its printed out in all movies
def test_create_movies_page(test_app):
    response = test_app.post('/movies', data = {
        'movie-name': 'Creed III', 
        'movie-director': 'Michael B. Jordan', 
        'ranking': 5
    }, follow_redirects = True)

    assert response.status_code == 200

    data = response.data.decode('utf-8')

    assert '<td>Creed III</td>' in data 
    assert '<td>Michael B. Jordan</td>' in data
    assert '<td>5</td> in data</td>' in data

#Test using a non-existent movie
def test_empty_movies_page(test_app):
    response = test_app.get('/movies')
    data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert '<td>' not in data

#Test using an edge case 
def test_movies_page_edge(test_app): 
    response = test_app.post('/movies', data = {
        'movie-name': 'Black Panther: Wakanda Forever',
        'movie-director': 'Ryan Coogler',
        'ranking': 5
    }, follow_redirectors = True)

    data = response.data.decode('utf-8')

    assert '<td>Black Panther: Wakanda Forever</td>' in data
    assert '<td>Ryan</td>' not in data 
    assert '<td>4</td>' not in data