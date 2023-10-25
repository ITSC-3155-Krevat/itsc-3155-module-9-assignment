# TODO: Feature 1

import pytest
from app import app, list_all_movies
from unittest.mock import patch

def test_list_all_movies():
    with patch('app.render_template') as mock_render_template:
        # Mocking the get_all_movies method from movie_repository
        with patch('app.movie_repository.get_all_movies') as mock_get_all_movies:
            # Setting the return value for mock_get_all_movies
            mock_get_all_movies.return_value = [
                {'title': 'Call Me By Your Name', 'director': 'Luca Guadagnino', 'rating': 5},
                {'title': 'Moonlight', 'director': 'Barry Jenkins', 'rating': 5}
            ]

            # Call the list_all_movies function
            list_all_movies()

            # Assert that render_template was called correctly
            mock_render_template.assert_called_once_with('list_all_movies.html', movies=mock_get_all_movies.return_value, list_movies_active=True)
