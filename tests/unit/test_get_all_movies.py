# TODO: Feature 1
from src.repositories.movie_repository import get_movie_repository

def test_get_all_movies():
    # Create a new blank movie repository instance and clear
    repo = get_movie_repository()
    repo.clear_db()

    # Add some movies to the repository
    movie1 = repo.create_movie('The Shawshank Redemption', 'Frank Darabont', 9.3)
    movie2 = repo.create_movie('The Godfather', 'Francis Ford Coppola', 9.2)

    # Call the get_all_movies method to 
    all_movies = repo.get_all_movies()

    # Assert that the returned dictionary contains the two movies we added
    assert len(all_movies) == 2
    assert movie1 in all_movies.values()
    assert movie2 in all_movies.values()