# TODO: Feature 1

from src.repositories.movie_repository import get_movie_repository

#initializing a test repository
test_repository = get_movie_repository()

#initializing test movies
movie1 = test_repository.create_movie('First movie', 'Director 1', 1)
movie2 = test_repository.create_movie('Second movie', 'Director 2', 2)
movie3 = test_repository.create_movie('Third movie', 'Director 3', 3)

#testing if all movies are obtained
def test_get_all():
    movies = []
    movies.append(test_repository.get_all_movies())

    assert movie1 in movies
    assert movie2 in movies
    assert movie3 in movies