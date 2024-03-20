def test_get_single_movie(movie_repository):
    # Assuming you have a movie already in the repository with ID 1
    movie = movie_repository.get_movie_by_id(1)
    assert movie is not None
    assert movie.title == 'Iron Man'
    assert movie.director == 'Jon Favreau'
    assert movie.rating == 5 
