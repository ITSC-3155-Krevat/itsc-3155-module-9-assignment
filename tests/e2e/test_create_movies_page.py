# TODO: Feature 2
from flask import Flask, app
from flask.testing import FlaskClient
import pytest
from app import app
# Making sure we have pytest on this venv
def test_this_works():
    assert 5 >  4
# passed

@pytest.fixture()
def test_app():
    return app.test_client()


# Testing the program works after passing in adequate values, 
def test_basic_func(test_app):
    response = test_app.get('/movies')
    assert response.status_code == 200
# works


def test_add_movie(test_app):
    response = test_app.post('/movies', data = {
        'movie_name' : 'Shrek',
        'director' : 'Andrew Adamson',
        'rating' : 5
    }, follow_redirects = True)
    assert response.status_code == 200
    assert 


