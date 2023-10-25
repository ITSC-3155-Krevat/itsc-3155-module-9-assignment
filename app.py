<<<<<<< HEAD
from flask import Flask, redirect, render_template, request, abort
=======
from flask import Flask, abort, redirect, render_template, request
>>>>>>> main

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)
app.debug = True
# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    global movie_repository
    temp_dict = movie_repository.get_all_movies()
    return render_template('list_all_movies.html', temp_dict = temp_dict, list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    title = request.form.get('title')
    director = request.form.get('director')
    rating = request.form.get('rating')

    if not title or not director or not rating or int(rating)>5 or int(rating)<1:
        return redirect('/movies/new')

    rating = int(rating)

    movie_repository.create_movie(title=title, director=director, rating=rating)
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    single_movie = movie_repository.get_movie_by_id(movie_id)
    if single_movie is None:
        abort(400)

    return render_template('get_single_movie.html', single_movie = single_movie, movie_id = movie_id)


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    global movie_repository
    movie_to_edit = movie_repository.get_movie_by_id(movie_id)
    if movie_to_edit is None:
        abort(404)
    return render_template('edit_movies_form.html', movie=movie_to_edit)


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    
    # TODO: Feature 5

    global movie_repository
    title = request.form.get('title')
    director = request.form.get('director')
    rating = request.form.get('rating')

    if title is None or director is None or rating is None or int(rating) > 5 or int(rating) < 1:
        abort(400)
    
    movie_repository.update_movie(movie_id, title, director, rating)
    # After updating the movie in the database, we redirect back to that single movie page
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    global movie_repository
    
    movie_to_delete = movie_repository.get_movie_by_id(movie_id)
    
    # If the movie with the given ID doesn't exist, return a 404 error
    if movie_to_delete is None:
        abort(404)
    movie_repository.delete_movie(movie_id)
    
    return redirect('/movies')
