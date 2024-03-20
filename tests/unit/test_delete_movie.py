# TODO: Feature 6
from src.repositories.movie_repository import get_movie_repository

movie_rep = get_movie_repository()

repo = get_movie_repository()
testmovie = repo.create_movie("Test", "George Lucas", 2)

def test_delete_movie():
    delete = repo.delete_movie(testmovie.movie_id)
    movie_check = movie_rep.get_movie_by_id(testmovie.movie_id)
    
    assert delete == testmovie
    assert testmovie != movie_check