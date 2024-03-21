# TODO: Feature 4

from src.repositories.movie_repository import get_movie_repository


#test cases
movie_repository = get_movie_repository()

movie1 = movie_repository.create_movie('harry potter', 'harry potter', '10')
movie2 = movie_repository.create_movie('the two towers', 'peter jackson', '10')


second_movie = movie_repository.get_movie_by_id(movie2.movie_id)
if (second_movie.movie_id == movie_repository.get_movie_by_id(movie2.movie_id)): 
    print("Success")

if (second_movie.movie_id != movie_repository.get_movie_by_id(movie2.movie_id)): 
    print("Error, mismatch")

movie_repository.clear_db()