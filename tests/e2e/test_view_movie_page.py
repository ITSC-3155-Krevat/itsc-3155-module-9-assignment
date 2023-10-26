# TODO: Feature 4
from src.repositories.movie_repository import get_movie_repository


def test_view_movie_page(test_app):
    movie = get_movie_repository()
    test_movie = movie.create_movie(title='test',director='john', rating=5)
    test_movie_id = test_movie.movie_id

    response = test_app.get(f'/movies/{test_movie_id}', follow_redirects=True)

    assert response.status_code == 200
    assert b'<td>test</td>' in response.data
    assert b'<td>john</td>' in response.data
    assert b'<td>5</td>' in response.data

def test_view_no_movie_page(test_app):
    movie = get_movie_repository()
    test_movie_id = movie.get_movie_by_id
    response = test_app.get(f'/movies/{test_movie_id}', follow_redirects=True)

    assert response.status_code == 404