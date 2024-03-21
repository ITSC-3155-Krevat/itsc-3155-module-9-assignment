# TODO: Feature 5
# test_app.py
from flask import url_for
from app import app  # Import your Flask app here
from src.repositories.movie_repository import get_movie_repository


def test_update_movie_endpoint_success(test_app):
        # Creating a movie to update
        #movie = self.repo.create_movie("Titanic", "Director One", 5)
    response = test_app.post('/movies/<int:movie_id>', data={
        'title': 'Updated Title',
        'director': 'Director One',
        'rating': 4
    }, follow_redirects = True)
    updated_movie = test_app.repo.get_movie_by_id()
    assert response.status_code == 200
    test_app.assertEqual(updated_movie.title, 'Updated Title')

def test_update_movie_endpoint_failure(self):
    # updating a movie that doesn't exist
    response = self.client.post(url_for('update_movie', movie_id=999), data={
        'title': 'Nonexistent Movie',
        'director': 'Director',
        'rating': 3,
    })
    self.assert404(response)


