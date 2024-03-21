# TODO: Feature 4
import unittest
from src.repositories.movie_repository import get_movie_repository

class getMovieByIDTestcase(unittest.TestCase):

    def test_retrieval(self):
        movie_repo = get_movie_repository
        movie1 = movie_repo.create_movie('the two towers','peter jackson','10')
        result = movie_repo.get_movie_by_id(movie1.movie_id)
        if (result.title != movie1.title):
            print("Help! Movie does not match database.")
        else:
            print("You passed!")

