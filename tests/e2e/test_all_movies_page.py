from app import app
import flask

def test_all_movies_page():
    test_app = app.test_client()
    with test_app.application.app_context():
        db = test_app.application.app_context().g.get(movie_repository)
    print (db)
    assert isinstance(db, dict)
