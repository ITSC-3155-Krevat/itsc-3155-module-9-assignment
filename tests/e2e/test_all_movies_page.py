from app import movie_repository

def test_all_movies_page(test_app):
    movie_repository.clear_db()
    movie_repository.create_movie("War of Worlds", "Me", 4)
    movie_repository.create_movie("War for Carrots", "Me", 3)
    movie_repository.create_movie("Harmony in Nature", "Me", 2)
    response = test_app.get("/movies")
    assert response.status_code == 200
    data = response.data.decode()
    assert '<th scope="col">id</th>' in data
    assert '<td>War of Worlds</td>' in data
    assert '<td>War for Carrots</td>' in data
    assert '<td>Harmony in Nature</td>' in data
    assert '<td>Me</td>' in data
    assert '<td>2</td>' in data
    assert '<td>3</td>' in data
    assert '<td>4</td>' in data
    movie_repository.clear_db()
    response = test_app.get("/movies")
    assert response.status_code == 200
    data = response.data.decode()
    assert '<h2 class = "ps-2 pt-2 pb-1">There are no movies saved yet.</h4>'
    
