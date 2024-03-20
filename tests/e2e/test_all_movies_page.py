from app import app, movie_repository


client = app.test_client()

def test_all_movies_valid_data():
    movie_repository.clear_db()
    # arrange
    movie_repository.create_movie('Silent Runnings', 'martin', 2)
    movie_repository.create_movie('Medium Runnings', 'cartin', 4)
    movie_repository.create_movie('Loud Runnings', 'fartin', 1)
    # act
    response = client.get('/movies')
    # assert
    assert response.status_code == 200
    assert b'<td>Silent Runnings</td>' in response.data
    assert b'<td>cartin</td>' in response.data
    assert b'<td>1</td>' in response.data


def test_all_movies_no_data():
    movie_repository.clear_db()
    # act
    response = client.get('/movies')
    # assert
    assert response.status_code == 200