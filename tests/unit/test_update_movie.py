# TODO: Feature 5
import random,string
from src.repositories.movie_repository import get_movie_repository

movie_repo = get_movie_repository()
    

def test_edit_movie():
    new_title = ''.join(random.choices(string.ascii_lowercase,k=11))
    new_director = ''.join(random.choices(string.ascii_lowercase,k=12))
    new_rating = random.randint(1,5)

    movie_repo.clear_db()
    movie =  movie_repo.create_movie("name","director",5)
    movie_repo.update_movie(movie.movie_id,new_title,new_director,new_rating)

    assert movie.director == new_director
    assert movie.title == new_title
    assert movie.rating == new_rating
