# TODO: Feature 6
from src.repositories.movie_repository import get_movie_repository
from app import app

def test_delete_movie():
    movie_repository = get_movie_repository()

    # Create a temporary movie to delete
    movie1 = movie_repository.create_movie('Kal Ho Na Ho', 'Raj Kapoor', 5)
    movie2 = movie_repository.create_movie('Jannat', 'Fawaz khan', 3)
    

    id1 = movie1.movie_id
    id2 = movie2.movie_id
    # This line is going to delete the movie
    movie_repository.delete_movie(id1)
    print(movie_repository.get_all_movies())
    # This line checks whethear the movie is deleted or not
    deleted_movie = movie_repository.get_movie_by_id(id1)
    assert deleted_movie is None
   