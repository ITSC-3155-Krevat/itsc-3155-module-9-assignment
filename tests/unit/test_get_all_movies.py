# TODO: Feature 1
from src.repositories.movie_repository import get_movie_repository

def test_get_all_movies():
    movie_repository = get_movie_repository()

    assert len(movie_repository.get_all_movies()) == 0
    movie_repository.create_movie('The Last Airbender', 'M. Night Shyamalan', 1)
    assert len(movie_repository.get_all_movies()) == 1
    movie_list = list(movie_repository.get_all_movies().items())
    
    movie1 = movie_list[0][1]
    assert movie1.movie_id == movie_list[0][0] 
    assert movie1.title == 'The Last Airbender'
    assert movie1.director == 'M. Night Shyamalan'
    assert movie1.rating == 1
    
    movie_repository.create_movie('Inception', 'Christopher Nolan', 4)
    assert len(movie_repository.get_all_movies()) == 2
    movie_list = list(movie_repository.get_all_movies().items())
    
    movie2 = movie_list[1][1]
    assert movie2.movie_id == movie_list[1][0] 
    assert movie2.title == 'Inception'
    assert movie2.director == 'Christopher Nolan'
    assert movie2.rating == 4

    movie_repository.delete_movie(movie1.movie_id)
    assert len(movie_repository.get_all_movies()) == 1
    movie_list = list(movie_repository.get_all_movies().items())
    assert movie2.movie_id == movie_list[0][0]

    movie_repository.clear_db()
    assert len(movie_repository.get_all_movies()) == 0