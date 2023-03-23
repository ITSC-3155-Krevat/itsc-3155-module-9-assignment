from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_id_with_movies():
    # Given a movie repository with at least one movie
    movie_repository = get_movie_repository()
    test_movie = movie_repository.create_movie('Interstellar', 'Christopher Nolan', 10)
    test_movie_id = test_movie.movie_id

    # When we attempt to retrieve the movie by its ID
    retrieved_movie = movie_repository.get_movie_by_id(test_movie_id)


    #  all attributes of the retrieved movie should match the original movie
    assert retrieved_movie.movie_id == test_movie_id
    assert retrieved_movie.title == 'Interstellar'
    assert retrieved_movie.director == 'Christopher Nolan'
    assert retrieved_movie.rating == 10
    
    # Delete the test movie after testing is complete
    movie_repository.delete_movie(test_movie_id)

def test_get_movie_by_id_with_empty_repository():
    # Given an empty movie repository
    movie_repository = get_movie_repository()

    # When we attempt to retrieve a movie by an ID
    retrieved_movie = movie_repository.get_movie_by_id(1)

    # Then the retrieved movie should be None
    assert retrieved_movie is None
