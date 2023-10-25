# TODO: Feature 2
from flask.testing import FlaskClient
import pytest
from app import app

@pytest.fixture()
def test_app():
    return app.test_client()


# Testing the program works after passing in adequate values, 
def test_basic_func(test_app):
    response = test_app.get('/movies')
    assert response.status_code == 200
# works