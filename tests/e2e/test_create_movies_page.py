# TODO: Feature 2

from src.repositories.movie_repository import get_movie_repository

def test_create_movie(test_app):

    # Clear db to test with fresh data
    movie_repository = get_movie_repository()
    movie_repository.clear_db()

    response = test_app.post('/movies', data={
        "name": "test movie name",
        "director-name": "test director name",
        "select-rating": 3
    }, follow_redirects=True)

    data = response.data.decode('utf-8')
    
    assert response.status_code == 200
    assert 'test movie name' in data
    assert 'test director name' in data

    #Tests if number of stars is equal to the movie rating added to db
    assert data.count('<i class="bi bi-star-fill"></i>') == 3

def test_create_movie_validation(test_app):
    response = test_app.post('/movies')
    assert response.status_code == 400   