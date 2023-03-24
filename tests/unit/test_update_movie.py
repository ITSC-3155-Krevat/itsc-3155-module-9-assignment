# TODO: Feature 5
from tests.e2e.conftest import test_app
from src.repositories.movie_repository import get_movie_repository
# Testing if the edit works
# Harry Potter: The Chamber of Secrets - David Yates - 3 -> Harry Potter: The Chamber of Secrets - David Yates - 5
def test_update_movie(test_app):
    movie_repository = get_movie_repository()
    temp_movie = movie_repository.create_movie('Harry Potter: The Chamber of Secrets', 'David Yates', 3)
    movie_id = temp_movie.movie_id


    updated_movie_data = {
    # Updated the rating from 3 to 5 with the same title and director of the movie
        'title': 'Harry Potter: The Chamber of Secrets',
        'director': 'Davis Yates',
        'rating': 5
    }
    # Updating all of the titles, director, and ratings
    response = test_app.post(f'/movies/{movie_id}', data=updated_movie_data)

    # Response status code to check for update correction
    assert response.status_code == 302 
    updated_movie = movie_repository.get_movie_by_id(movie_id)
    assert updated_movie.title == updated_movie_data['title']
    assert updated_movie.director == updated_movie_data['director']
    assert updated_movie.rating == updated_movie_data['rating']