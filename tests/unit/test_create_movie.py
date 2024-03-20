# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_create_movie():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    
    movie_repository.create_movie('The Shawshank Redemption', 'Frank Darabont', 9.2)
    
    movies = movie_repository.get_all_movies()
    
    assert isinstance(movies, dict)
    
    added_movie = movies.get(1)
    
    print("Movies in dictionary:", movies)
    assert added_movie is not None, "Movie not in dictionary"
    
    assert added_movie.title == 'The Shawshank Redemption'
    assert added_movie.director == 'Frank Darabont'
    assert added_movie.rating == 9.2