from app import app, movie_repository

def test_create_movie_valid_data():
    movie_repository.clear_db()

    with app.test_client() as client:
        movie_data = {
            "title": "The fat and the furious",
            "director": "Vin Gasoline",
            "rating": "5"
        }
        
        response = client.post('/movies', data=movie_data)
        
    assert response.status_code == 302
    movies = movie_repository.get_all_movies()
    assert len(movies) == 1
    
    movie = next(iter(movies.values()))
    assert movie.title == movie_data["title"]
    assert movie.director == movie_data["director"]
    assert movie.rating == int(movie_data["rating"])

def test_create_movie_invalid_rating():
    movie_repository.clear_db()

    with app.test_client() as client:
        movie_data = {
            "title": "The Matrix downloaded",
            "director": "Andrew Tate",
            "rating": "7"  
        }
        
        response = client.post('/movies', data=movie_data)
        
    assert response.status_code == 400
    movies = movie_repository.get_all_movies()
    assert len(movies) == 0
    
def test_create_movie_missing_fields():
    movie_repository.clear_db()

    
    with app.test_client() as client:
        movie_data = {
            "title": "Underwater",
            
            "rating": "4"
        }
        
        response = client.post('/movies', data=movie_data)
        
    assert response.status_code == 400
    movies = movie_repository.get_all_movies()
    assert len(movies) == 0

from app import app, movie_repository

def test_create_movie_empty_title():
    movie_repository.clear_db()

    with app.test_client() as client:
        movie_data = {
            "title": "",
            "director": "Michael Bay",
            "rating": "5"
        }
        
        response = client.post('/movies', data=movie_data)
        
    assert response.status_code == 400
    movies = movie_repository.get_all_movies()
    assert len(movies) == 0

def test_create_movie_empty_director():
    movie_repository.clear_db()

    with app.test_client() as client:
        movie_data = {
            "title": "Underwater",
            "director": "",
            "rating": "5"
        }
        
        response = client.post('/movies', data=movie_data)
        
    assert response.status_code == 400
    movies = movie_repository.get_all_movies()
    assert len(movies) == 0
