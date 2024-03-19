from flask import Flask, redirect, render_template, request, url_for

from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    movie_repo = get_movie_repository()
    all_movies = movie_repo.get_all_movies()
    movies_list = [
        {"id": movie_id, "title": movie.title, "director": movie.director, "rating": movie.rating}
        for movie_id, movie in all_movies.items()
    ]

    return render_template('list_all_movies.html', list_movies_active=True, movies=movies_list)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    # when movie in movie page is clicked, get request is made
    # this sends the movie_id 
    
    movie = movie_repository.get_movie_by_id(movie_id)
    return render_template('get_single_movie.html', movie=movie)


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    return render_template('edit_movies_form.html')


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    movie_repository.delete_movie(movie_id)
    return render_template('list_all_movies.html')