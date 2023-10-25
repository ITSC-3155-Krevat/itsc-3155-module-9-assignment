# TODO: Feature 1
from app import app
from src.repositories.movie_repository import get_movie_repository

#test to see method gets all movies when there are none and when there are multiple
def test_get_all_movies():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    temp_dict = movie_repository.get_all_movies()
    assert len(temp_dict) == 0


    movie1 = movie_repository.create_movie('spiderman', 'Sam Raimi', 5)
    movie2 = movie_repository.create_movie('Batman', 'Zaid Jebril', 3)
    movie3 = movie_repository.create_movie('Superman', 'Sam Smith', 4)

    temp_dict = movie_repository.get_all_movies()
    assert len(temp_dict) == 3
    movie_repository.clear_db()

#test to see method gets all correct movies
def test_get_all_correct_movies():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()

    movie2 = movie_repository.create_movie('Batman', 'Zaid Jebril', 3)
    movie2_id = movie2.movie_id
    movie3 = movie_repository.create_movie('Superman', 'Sam Smith', 4)
    movie3_id = movie3.movie_id

    temp_dict = movie_repository.get_all_movies()    

    assert temp_dict[movie2_id] == movie2
    assert temp_dict[movie3_id] == movie3
    movie_repository.clear_db()






