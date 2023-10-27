# TODO: Feature 5
from flask import Flask, app
from flask.testing import FlaskClient
import pytest,string,random
from app import app
from src.repositories.movie_repository import get_movie_repository


@pytest.fixture()
def test_app():

    return app.test_client()

movie_repo = get_movie_repository()

#Large test because why not
def test_update_movie(test_app):
    

    movie_repo.clear_db()

    #Feilds to be changed
    old_title = ''.join(random.choices(string.ascii_lowercase,k=11))
    old_director = ''.join(random.choices(string.ascii_lowercase,k=12))
    old_rating = random.randint(1,5)

    #Feilds to be changed to 
    new_title = ''.join(random.choices(string.ascii_lowercase,k=11))
    new_director = ''.join(random.choices(string.ascii_lowercase,k=12))
    new_rating = (random.randint(1,5))

    #tuple to check if changed values are present in the new html data 
    byte_tuple = (new_title.encode(),new_director.encode(), str(new_rating).encode)

    #create a new dummy movie
    movie = movie_repo.create_movie(old_title,old_director,old_rating)
    movie_id = movie.movie_id


    #Post new feilds to server and check if changes are retained
    response = test_app.post(f'/movies/{movie_id}', data = {
        'movie_name' : new_title,
        'director' : new_director,
        'rating' : new_rating
    },follow_redirects = True)

    assert all(item for item in byte_tuple)
    assert movie.title == new_title
    assert movie.director == new_director
    assert movie.rating == new_rating
    assert response.status_code == 200
    




    




    





    


    



    






    