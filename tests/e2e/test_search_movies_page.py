# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository


def test_view_movie_info(test_app):
    movie = get_movie_repository() 
    test_movie = movie.create_movie("test movie", "test director", 5)
    test_movie_title = movie.get_movie_by_title

    response = test_app.get(f'/movies/{test_movie_title}', follow_redirects=True)

    assert response.status_code == 200
    assert b'<td>test movie</td>' in response.data
    assert b'<td> test director </td>' in response.data
    assert b'<td> 5 </td>' in response.data

def test_view_empty_movie(test_app): 
    movie = get_movie_repository()
    test_movie_title = movie.get_movie_by_title
    response = test_app.get(f'/movies/{test_movie_title}', follow_redirects=True)

    assert response.status_code == 404 