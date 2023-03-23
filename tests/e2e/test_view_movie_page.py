# TODO: Feature 4: As a user, I should be able to view a movie in isolation and have access to edit and delete that movie.

from flask import url_for

from repositories import movie_repository


def test_view_movie_page(client, movie):
    response = client.get(url_for('get_single_movie', movie_id=movie.id))
    assert response.status_code == 200
    assert movie.title in str(response.data)  # Make sure the movie title is displayed on the page

def test_edit_movie_page(client, movie):
    response = client.get(url_for('get_edit_movies_page', movie_id=movie.id))
    assert response.status_code == 200
    assert movie.title in str(response.data)  # Make sure the movie title is pre-populated in the form

def test_update_movie(client, movie):
    updated_title = 'Updated Title'
    response = client.post(url_for('update_movie', movie_id=movie.id), data={'title': updated_title})
    assert response.status_code == 302  # Expect a redirect
    updated_movie = movie_repository.get_movie(movie.id)
    assert updated_movie.title == updated_title  # Make sure the movie title was updated in the database

def test_delete_movie(client, movie):
    response = client.post(url_for('delete_movie', movie_id=movie.id))
    assert response.status_code == 302  # Expect a redirect
    assert movie_repository.get_movie(movie.id) is None  # Make sure the movie was deleted from the database

