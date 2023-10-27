from src.repositories.movie_repository import  get_movie_repository

def test_get_all_movies():
    movie_repo = get_movie_repository()
    movie_repo.clear_db()
    movie_repo.create_movie("The War", "Me", 5.0)
    assert len(movie_repo.get_all_movies()) == 1
    assert isinstance(movie_repo.get_all_movies(), dict)
    movie_repo.create_movie("The Peace", "Also Me", 2.5)
    assert len(movie_repo.get_all_movies()) == 2
    movie_repo.create_movie("Another Movie", "Me Again", 2.5)
    movie_repo.create_movie("Another Movie", "Me Again", 2.5)
    movie_repo.create_movie("Another Movie", "Me Again", 2.5)
    count = 0
    for movie in movie_repo.get_all_movies().values():
        if movie.title == "Another Movie" and movie.director == "Me Again":
            count += 1
    assert count == 3
    assert movie_repo._db == movie_repo.get_all_movies()