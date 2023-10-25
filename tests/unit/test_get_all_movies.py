# TODO: Feature 1
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie


def test_get_all_movies():
    movie_list_1 = [
        {
            "title": "Aliens",
            "director": "James Cameron",
            "rating": "5"
            
        }, 
        {
            "title": "Suicide Squad", 
            "director": "David Ayer",
            "rating": "3"
        },
        {
            "title": "A Quiet Place",
            "director": "John Krasinski",
            "rating": "4"
        },
        {
            "title": "Pitch Perfect",
            "director": "Jason Moore",
            "rating": "2"
        }
    ]

    movie_repo = get_movie_repository()

    for movie_data in movie_list_1:
        movie_repo.create_movie(movie_data["title"], movie_data["director"], int(movie_data["rating"]))

    test_list_1 = movie_repo.get_all_movies()
    
    test_list_2 = [
        Movie(1, "Aliens", "James Cameron", 5),
        Movie(2, "Suicide Squad", "David Ayer", 3),
        Movie(3, "A Quiet Place", "John Krasinski", 4),
        Movie(4, "Pitch Perfect", "Jason Moore", 2)
    ]

    for test_movie_1, test_movie_2 in zip(test_list_1.values(), test_list_2):
        assert test_movie_1.title == test_movie_2.title
        assert test_movie_1.director == test_movie_2.director
        assert test_movie_1.rating == test_movie_2.rating