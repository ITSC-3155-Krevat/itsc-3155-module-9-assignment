# TODO: Feature 3
# Gage Brown

from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_title_with_movies():
    # Given a movie repository with at least one movie
    movie_repository = get_movie_repository()
    test_movie = movie_repository.create_movie('Interstellar', 'Christopher Nolan', 10)
    test_movie_title = test_movie.title

    # When we attempt to retrieve the movie by its ID
    retrieved_movie = movie_repository.get_movie_by_title(test_movie_title)

  
    # all attributes of the retrieved movie should match the original movie
    assert retrieved_movie.title == 'Interstellar'
    assert retrieved_movie.director == 'Christopher Nolan'
    assert retrieved_movie.rating == 10
    
    

def test_get_movie_by_title_with_empty_repository():
    # Given an empty movie repository
    movie_repository = get_movie_repository()

    # When we attempt to retrieve a movie by an ID
    retrieved_movie = movie_repository.get_movie_by_title('Spider')

    # Then the retrieved movie should be None
    assert retrieved_movie is None
