import pytest
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture
def movie_repo():
    repo = get_movie_repository()  # get and clear the movie repository
    repo.clear_db()
    return repo

def test_single_view_found(test_app, movie_repo):  # renamed from test_view_single_movie_page_e2e
    movie_repo.clear_db()  # clear the database and create a new movie
    created_movie = movie_repo.create_movie("Inception", "Christopher Nolan", 8)
    
    response = test_app.get(f"/movies/{created_movie.movie_id}")  # make a get request for the created movie
    
    # check if the response has the movie's details
    assert response.status_code == 200
    assert b"Inception" in response.data
    assert b"Christopher Nolan" in response.data
    assert b"Rating: 8" in response.data
    assert b"Edit" in response.data  # check for edit button/link
    assert b"Delete" in response.data  # check for delete button/link

def test_single_view_not_found(test_app, movie_repo):  # renamed from test_view_single_movie_page_not_found_e2e
    movie_repo.clear_db()  # clear the database to ensure no movie exists
    
    response = test_app.get("/movies/999")  # make a get request for a non-existent movie
    
    # check if the response indicates the movie was not found
    assert response.status_code == 404
    assert b"Movie not found" in response.data