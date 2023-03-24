# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository

#Create a movie and test if it exists in the respository 
def test_create_movie_implementation():
    movies = get_movie_repository()
    movies.clear_db()
    test_case = movies.create_movie('The Batman', 'Matt Reeves', 5)

    assert test_case == movies.get_movie_by_title('The Batman')

#Test against a non-existent movie 
def test_create_movie_empty(): 
    movies = get_movie_repository()
    test_case = movies.create_movie('Spiderman: No Way Home', 'Jon Watts', 2)
    movies.clear_db()
    assert movies.get_movie_by_title('Spiderman: No Way Home') == None
#Test from a loaded repository 

def test_create_movie_full(): 
    movies = get_movie_repository()
    movie_1 = movies.create_movie('Movie 1', 'Director 1', 1)
    movie_2 = movies.create_movie('Movie 2', 'Director 2', 2)
    movie_3 = movies.create_movie('Movie 3', 'Director 3', 3)
    movie_4 = movies.create_movie('Movie 4', 'Director 4', 4)
    movie_5 = movies.create_movie('Movie 5', 'Director 5', 5)

    assert movies.get_movie_by_title('Movie 1') == movie_1
    assert movies.get_movie_by_title('Movie 2') == movie_2
    assert movies.get_movie_by_title('Movie 3') == movie_3
    assert movies.get_movie_by_title('Movie 4') == movie_4
    assert movies.get_movie_by_title('Movie 5') == movie_5

