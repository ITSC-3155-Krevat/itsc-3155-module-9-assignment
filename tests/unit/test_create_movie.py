# TODO: Feature 2

from app import create_movie

def test_create_movie():
    movie = create_movie('Star Wars', 'George Lucas', 5)

    assert movie.title == 'Star Wars'
    assert movie.director == 'George Lucas'
    assert movie.rating == 5