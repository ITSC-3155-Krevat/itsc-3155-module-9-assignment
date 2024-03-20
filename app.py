from flask import Flask, redirect, render_template, request, url_for

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()
get_movie_repository()

# # Hardcoded test data
# TEST_MOVIES = [
#     {'title': 'Avatar', 'director': 'James Cameron', 'rating': 7},
#     {'title': 'Inception', 'director': 'Christopher Nolan', 'rating': 8},
#     {'title': 'The Shawshank Redemption', 'director': 'Frank Darabont', 'rating': 9}
# ]

# # Populate repository with hardcoded test data
# for movie_data in TEST_MOVIES:
#     movie_repository.create_movie(movie_data['title'], movie_data['director'], movie_data['rating'])


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
     # TODO: Feature 1
    movies = movie_repository.get_all_movies()
    return render_template('list_all_movies.html', movies=movies, list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)
    
@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')

@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)

@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    movie = movie_repository.get_movie_by_id(movie_id)
    return render_template('get_single_movie.html', movie=movie)


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    movie = movie_repository.get_movie_by_id(movie_id)
    return render_template('edit_movies_form.html', movie=movie)