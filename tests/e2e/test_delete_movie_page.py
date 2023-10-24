# TODO: Feature 6
# TODO: Feature 6
from app import app
from src.repositories.movie_repository import get_movie_repository

test_app = app.test_client()

def test_The_delete_movie():
    movie_repository = get_movie_repository()
    # Clear database
    movie_repository.clear_db()
    movie1 = movie_repository.create_movie('Kal Ho Na Ho', 'Fawaz', 5)
    movie2 = movie_repository.create_movie('Mann', 'Kidwai', 4)
    movie_repository._db[0] = movie1
    movie_repository._db[1] = movie2
    response = test_app.post(f'/movies/{movie1.movie_id}/delete')
    assert response.status_code == 200 
    del_movie1 = movie_repository.get_movie_by_id(movie1.movie_id)
    del_movie2 = movie_repository.get_movie_by_id(movie2.movie_id)

    assert del_movie1 is None
    assert del_movie2 is not None
