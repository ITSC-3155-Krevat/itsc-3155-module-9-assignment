# TODO: Feature 1
import pytest
from app import app
from src.repositories.movie_repository import get_movie_repository

movie_repo = get_movie_repository()

@pytest.fixture()
def app_test():
    return app.test_client()

def test_all_movies_page(app_test):
    movie_repo.create_movie("John Wick", "Chad Stahelski", 4)
    movie_repo.create_movie("Air Force One", "Wolfgang Petersen", 5)
    movie_repo.create_movie("The Dark Knight", "Christopher Nolan", 5)
    find_movie1 = movie_repo.get_movie_by_title("John Wick")
    title1 = find_movie1.title
    director1 = find_movie1.director
    rating1 = find_movie1.rating
    find_movie2 = movie_repo.get_movie_by_title("Air Force One")
    title2 = find_movie2.title
    director2 = find_movie2.director
    rating2 = find_movie2.rating
    find_movie3 = movie_repo.get_movie_by_title("The Dark Knight")
    title3 = find_movie3.title
    director3 = find_movie3.director
    rating3 = find_movie3.rating
    
    response = app_test.get('/movies')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert f'<td>{title1}</td>' in response_data
    assert f'<td>{director1}</td>' in response_data
    assert f'<td>{rating1}</td>' in response_data
    
    assert f'<td>{title2}</td>' in response_data
    assert f'<td>{director2}</td>' in response_data
    assert f'<td>{rating2}</td>' in response_data
    
    assert f'<td>{title3}</td>' in response_data
    assert f'<td>{director3}</td>' in response_data
    assert f'<td>{rating3}</td>' in response_data

