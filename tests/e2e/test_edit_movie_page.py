from app import app
from src.repositories.movie_repository import get_movie_repository

# TODO: Feature 5 
def test_edit_movie():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    tester = app.test_client()
    movie1 = movie_repository.create_movie('The Matrix', 'Wachowski', 5)
    response = tester.post(
      f'/movies/{movie1.movie_id}',
      data = dict(title="Avatar", director="James Cameron", rating="5", login_form="movie_form"),
      follow_redirects=True
      )
    assert response.status_code == 200
    assert b'<td>Avatar</td>' in response.data
    assert b'<td>James Cameron</td>' in response.data
    assert b'<td>5</td>' in response.data

    assert b'<td>The Matrix</td>' not in response.data