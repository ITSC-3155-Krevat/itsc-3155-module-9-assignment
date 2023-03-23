from app import app
from src.repositories.movie_repository import get_movie_repository

# TODO: Feature 2 [DONE]
def test_create_movie():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()

    #Test that no movies exist in database
    assert len(movie_repository.get_all_movies()) == 0

    #Test that one object is created by create_movie function 
    movie1 = movie_repository.create_movie('Chef', 'Jon Favreau', 3)
    assert len(movie_repository.get_all_movies()) == 1
    movie2 = movie_repository.create_movie('The Darjeeling Limited', 'Wes Anderson', 4)
    assert len(movie_repository.get_all_movies()) == 2

    #Test that input is correctly saved into the Movie object
    assert movie1.title == 'Chef'
    assert movie1.director == 'Jon Favreau'
    assert movie1.rating == 3

    assert movie2.title == 'The Darjeeling Limited'
    assert movie2.director == 'Wes Anderson'
    assert movie2.rating == 4

     #Clear database
    movie_repository.clear_db()