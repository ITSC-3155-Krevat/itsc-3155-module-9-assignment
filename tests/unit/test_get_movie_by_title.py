# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository

# creating a movie repository
temp_movie_repository = get_movie_repository()

# adding movies to the movie repository
temp_movie_repository.create_movie('Movie A', 'Director A', 1)
temp_movie_repository.create_movie('Movie B', 'Director B', 2)
temp_movie_repository.create_movie('Movie C', 'Director C', 3)
temp_movie_repository.create_movie('Movie D', 'Director D', 4)

def test_get_movie_by_title():

    # testing if you can get an existing movie by it's title
    movie_test_1 = temp_movie_repository.get_movie_by_title('Movie A')
    assert movie_test_1.title == 'Movie A'

    movie_test_2 = temp_movie_repository.get_movie_by_title('Movie B')
    assert movie_test_2.title == 'Movie B'

    movie_test_3 = temp_movie_repository.get_movie_by_title('Movie C')
    assert movie_test_3.title == 'Movie C'

    movie_test_4 = temp_movie_repository.get_movie_by_title('Movie D')
    assert movie_test_4.title == 'Movie D'

    # testing if you can get a nonexisting movie by it's title
    movie_test_5 = temp_movie_repository.get_movie_by_title('Moive F')
    assert movie_test_5 == None
