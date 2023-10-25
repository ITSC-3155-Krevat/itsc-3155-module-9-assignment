# TODO: Feature 1
from src.repositories import movie_repository

def test_get_all_movies():
    # get movie dict
    movies = movie_repository.get_movie_repository()

    # test whether the dict is empty
    assert len(movies.get_all_movies()) == 0

    # create movies
    movies.create_movie("SomeTitle1", "SomeDirector1", 5)
    movies.create_movie("SomeTitle2", "SomeDirector2", 1)
    movies.create_movie("SomeTitle3", "SomeDirector3", 3)
    movies.create_movie("SomeTitle4", "SomeDirector4", 2)
    movies.create_movie("SomeTitle5", "SomeDirector5", 4)

    # check whether movie dict contains 5 movies
    assert len(movies.get_all_movies()) > 0
    assert len(movies.get_all_movies()) == 5