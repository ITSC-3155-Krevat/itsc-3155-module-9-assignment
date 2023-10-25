from flask import Flask, redirect, render_template, request, make_response

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True, movies=movie_repository.get_all_movies())


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2

    # getting data from form
    movie_name = request.form.get('movieName')
    director = request.form.get('director')
    rating = request.form.get('rating', type=int)

    # validating data
    if not movie_name or not director or rating not in range(1,6):
        response = make_response("Invalid input", 400)
        return response
    
    # saving movie rating to movie repo
    movie_repository.create_movie(movie_name, director, rating)

    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    # Fetch the movie details from the repository using the movie_id
    movie = movie_repository.get_movie_by_id(movie_id)

    # Check if the movie exists
    if not movie:
        return "Movie not found", 404
    
    # Render the template and pass the movie details
    return render_template('get_single_movie.html', movie=movie)

@app.delete('/movies/<int:movie_id>')
def delete_movie(movie_id: int):
    # Fetch the movie repository instance
    movie_repo = movie_repository.get_movie_repository()

    # Attempt to delete the movie from the repository
    try:
        movie_repo.delete_movie(movie_id)
    except ValueError:
        return "Movie not found or could not be deleted", 404
    
    # Redirect back to the list of all movies
    return redirect('/movies')

# Fetch existing movie details and show edit form
@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):

    movie = movie_repository.get_movie_by_id(movie_id)
    if not movie:
        return "Movie not found", 404
    return render_template('edit_movie_form.html', movie=movie)

# Handle edit form submission
@app.post('/movies/<int:movie_id>/edit')
def post_edit_movies_page(movie_id: int):
    updated_data = request.form
    success = movie_repository.update_movie_by_id(movie_id, updated_data)
    if not success:
        return "Could not update movie", 400
    return redirect(f'/movies/{movie_id}')

