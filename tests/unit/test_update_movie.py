from src.models.movie import Movie


def test_update_movie():
    # Setup: Create a repository and add a test movie
  def test_movie_model():
    movie = Movie(123, 'Star Wars', 'George Lucas', 5)
    # Update the movie
    updated_title = "Updated Star Wars"
    updated_director = "Updated George Lucas"
    updated_rating = 3
    movie.update_movie(movie.id, updated_title, updated_director, updated_rating)
    
    assert movie.movie_id == 123
    assert updated_title.title == 'Updated Star Wars'
    assert updated_director.director == 'Updated George Lucas'
    assert updated_rating.rating == 3