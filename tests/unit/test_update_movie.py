# TODO: Feature 5

from tests.e2e.conftest import test_app
from src.repositories.movie_repository import get_movie_repository


def test_update_movie(test_app):
   # Arrange
   movie_repository = get_movie_repository()
   test = movie_repository.create_movie('Toy Story', 'John Lasster',3)
   movie_id = test.movie_id

   updated = {
      'title': 'Toy Story 2', 'director': 'John Lasser', 'rating': 4
   }

   movie_repository.update_movie(updated)
   update_movie = movie_repository.get_movie_by_id(movie_id)

   # Assert
   assert update_movie.title == 'Toy Story 2'
   assert update_movie.director == 'John Lasser'
   assert update_movie.rating == 4