# TODO: Feature 1
import pytest
from app import app
from src.models.movie import Movie

def test_all_movies():
    test_client = app.test_client()
    temp_movie = Movie(1, 'Spiderman', 'Zaid', 5)
    response = test_client.post('/movies', data = {
        1 : temp_movie
    })

    data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert b'<td>1</td' in response.data
    assert b'<td>SpiderMan</td' in response.data
    assert b'<td>5</td'in response.data