# TODO: Feature 1
from app import app
from src.repositories.movie_repository import get_movie_repository

# Base test for list all movies
def test_list_all_movies():

    client = app.test_client()
    response = client.get('/movies')
    assert response.status_code == 200

    data = response.data.decode('utf-8')
    assert 'All Movies' in data

# Tests list all ensuring repo has data
def test_list_all_movies_with_data():
    repo = get_movie_repository()

    # Adds mock data to repo
    repo.create_movie('The Shawshank Redemption', 'Frank Darabont', 4)
    repo.create_movie('The Godfather', 'Francis Ford Coppola', 3)
    repo.create_movie('The Godfather: Part II', 'Francis Ford Coppola', 5)

    # Checks if the page is retrieved correctly
    client = app.test_client()
    response = client.get('/movies')
    assert response.status_code == 200

    # Retrieves html repsonse and formats it correctly
    data = response.data.decode('utf-8')
    repo.get_all_movies()

    # Iterates through every key in the dictionary and checks if the value exists in the html response
    for id in repo.get_all_movies().keys():
        assert repo.get_movie_by_id(id).title in data
        assert repo.get_movie_by_id(id).director in data

    # Checks if the total stars on the page is equal to all the movie ratings added together
    total_stars = data.count('<i class="bi bi-star-fill"></i>')
    total_ratings = sum([movie.rating for movie in repo.get_all_movies().values()])
    assert total_stars == total_ratings

    # Checks to see if the amount of info links is equal to total repo entries
    assert len(repo.get_all_movies()) == data.count('<i class="bi bi-info-circle"></i>')

# Tests list all movies ensuring repo is clear
def test_list_all_movies_without_data():

    # Pulls movie repository and clears it 
    repo = get_movie_repository()
    repo.clear_db()
    
    # Checks if the page is retrieved correctly
    client = app.test_client()
    response = client.get('/movies')
    assert response.status_code == 200

    # Retrieves html response and formats it correctly
    data = response.data.decode('utf-8')

    # Checks if the table is empty
    assert '<td>' not in data
    