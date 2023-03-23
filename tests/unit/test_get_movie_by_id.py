from app import app
from src.repositories.movie_repository import get_movie_repository

# TODO: Feature 4

def test_create_movie():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()

    #create movie object
    movie1 = movie_repository.create_movie('Transformer', 'Mike Bay', 2)

    #Create new movie object by using get_movie_by_id function
    # with the movie object created by create_movie function
    movie2 = movie_repository.get_movie_by_id(movie1.movie_id)

    #compare movie.id == movie2.id
    assert movie1.movie_id == movie2.movie_id

    #obtain movie object by using get_movie_by_id function from a movie that doesn't exist
    movie2 = movie_repository.get_movie_by_id(12345)
    assert  movie2 == None


