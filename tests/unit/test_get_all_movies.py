from app import movie_repository


def test_get_movies_valid_data():
    movie_repository.clear_db()
    # arrange
    movie_repository.create_movie('Silent Runnings', 'martin', 2)
    movie_repository.create_movie('Medium Runnings', 'cartin', 4)
    movie_repository.create_movie('Loud Runnings', 'fartin', 1)
    # act
    response = movie_repository.get_all_movies()
    movies = response.items()
    # assert
    assert len(response.items()) == 3


def test_get_movies_no_data():
    movie_repository.clear_db()    
    # act
    response = movie_repository.get_all_movies()
    movies = response.items()
    # assert
    assert len(movies) == 0