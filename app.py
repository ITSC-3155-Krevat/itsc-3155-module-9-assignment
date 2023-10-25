from flask import Flask, redirect, render_template, request, abort

from src.repositories.movie_repository import get_movie_repository


app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    movies = movie_repository.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, movies=movies)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    entered_movie_name = request.form.get('name')
    entered_director_name = request.form.get('director-name')
    entered_rating = request.form.get('select-rating')
    if not entered_movie_name:
        abort(400)
    if not entered_director_name:
        abort(400)
    if not entered_rating:
        abort(400)
    entered_rating = int(entered_rating)
    movie_repository.create_movie(entered_movie_name,entered_director_name,entered_rating)
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    return render_template('get_single_movie.html')


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
    pass