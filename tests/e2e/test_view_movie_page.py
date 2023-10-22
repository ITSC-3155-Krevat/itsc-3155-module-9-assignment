from app import app
from src.repositories.movie_repository import get_movie_repository

# TODO: Feature 4
def test_get_single_movie():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    movie1 = movie_repository.create_movie('Chef', 'Jon Favreau', 3)
    tester = app.test_client()
    response = tester.get(f'/movies/{movie1.movie_id}/edit', data={'action': 'clicked'})
    assert response.status_code == 200
    assert b'<label for="title" class="form-label">Movie Name</label>' in response.data
    
    
    
