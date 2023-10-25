# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository

def test_create_movie():
    create_movies = get_movie_repository()
    create_movies.create_movie('Dilwale', 'Rohit Sheety', '4.5')
    movie = create_movies.get_movie_by_title('Dilwale')
    assert movie in create_movies._db.values()

def test_missing_fields():
    create_movies = get_movie_repository()
    create_movies.create_movie('', '', '')
    movie = create_movies.get_movie_by_title('')
    # assert movie not in create_movies._db.values()
    pass
    # assertIsNone(movie)
    
    
def invalid_rating():
    create_movies = get_movie_repository()
    create_movies.create_movie('Dilwale', 'Rohit Sheety', '5.5')
    pass
