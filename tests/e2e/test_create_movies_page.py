import html

def test_create_movie(test_app):
    movie_data = {
        "title": "The fat and the furious",
        "director": "Vin Gasoline",
        "rating": "5"
    }

    response = test_app.post('/movies', data=movie_data, follow_redirects=True)
    data = response.data.decode('utf-8')
    
    assert response.status_code == 200
    assert "The fat and the furious" in data  

def test_create_movie_invalid_rating(test_app):
    movie_data = {
        "title": "The Matrix downloaded",
        "director": "Andrew Tate",
        "rating": "7"  
    }

    response = test_app.post('/movies', data=movie_data)
    
    assert response.status_code == 400

def test_create_movie_missing_data(test_app):

    movie_data = {
        "title": "Jeepers Creepers",
        "rating": "5"
    }  

    response = test_app.post('/movies', data=movie_data)
    
    assert response.status_code == 400


def test_create_movie_special_characters(test_app):
    special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "<", ">"]
    
    for char in special_characters:
    
        movie_data = {
            "title": f"Test{char}",
            "director": "Who",
            "rating": "3"
        }

        response = test_app.post('/movies', data=movie_data)

        assert response.status_code == 302  

        list_response = test_app.get('/movies')
        data = list_response.data.decode('utf-8')

        assert f"Test{char}" in data or f"Test{html.escape(char)}" in data



def test_create_movie_and_verify_in_list(test_app):

    movie_data = {
        "title": "Underwater",
        "director": "Ryan Smith",
        "rating": "4"
    }

    response = test_app.post('/movies', data=movie_data)
    
    assert response.status_code == 302  

    list_response = test_app.get('/movies')
    data = list_response.data.decode('utf-8')

    assert movie_data["title"] in data


def test_create_movie_empty_title(test_app):
    movie_data = {
        "title": "",
        "director": "Vin Gasoline",
        "rating": "5"
    }

    response = test_app.post('/movies', data=movie_data)
    assert response.status_code == 400

def test_create_movie_empty_director(test_app):
    movie_data = {
        "title": "The fat and the furious",
        "director": "",
        "rating": "5"
    }

    response = test_app.post('/movies', data=movie_data)
    assert response.status_code == 400

def test_create_movie_empty_rating(test_app):
    movie_data = {
        "title": "The fat and the furious",
        "director": "Vin Gasoline",
        "rating": ""
    }

    response = test_app.post('/movies', data=movie_data)
    assert response.status_code == 400

def test_create_movie_whitespace_title(test_app):
    movie_data = {
        "title": "   ",
        "director": "Vin Gasoline",
        "rating": "5"
    }

    response = test_app.post('/movies', data=movie_data)
    assert response.status_code == 400

def test_create_movie_non_numeric_rating(test_app):
    movie_data = {
        "title": "The fat and the furious",
        "director": "Vin Gasoline",
        "rating": "five"
    }

    response = test_app.post('/movies', data=movie_data)
    assert response.status_code == 400
