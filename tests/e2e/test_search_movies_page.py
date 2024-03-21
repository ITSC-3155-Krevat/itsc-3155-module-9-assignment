# TODO: Feature 3

from app import app

def test_search_movies():
    test_app = app.test_client()
    test_app.post("/movies", data={
        "title" : "My_movie",
        "director" : "Myself",
        "rating" : 80
    })
    response = test_app.get("/movies/search", query_string={
        "title" : "My_movie",
        "director" : "Myself",
        "rating" : 80})
    assert b'<h1>My_movie</h1>' in response.data
    assert b'<h2>Myself</h2>' in response.data
    assert b'<h3>80</h3>' in response.data