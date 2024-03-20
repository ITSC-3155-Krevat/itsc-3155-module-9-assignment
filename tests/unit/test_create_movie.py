from src.repositories.movie_repository import get_movie_repository

def test_create_movie():

    movie_repository = get_movie_repository()
    initial_movie_count = len(movie_repository.get_all_movies())
    movie_repository.create_movie("Test Movie", "Test Director", 3)
    assert len(movie_repository.get_all_movies()) == initial_movie_count + 1
    new_movie = movie_repository.get_movie_by_title("Test Movie")
    assert new_movie is not None
    assert new_movie.title == "Test Movie"
    assert new_movie.director == "Test Director"
    assert new_movie.rating == 3