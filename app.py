from flask import Flask, redirect, render_template

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
    movies = [
        {'title': 'Everything Everywhere All at Once', 'rating': 9.7},
        {'title': 'Avatar', 'rating': 8.6},
        {'title': 'Interstellar', 'rating': 9.5},
        {'title': 'La La Land', 'rating': 9.1},
        {'title': 'Corpse Bride', 'rating': 8.2},
        {'title': 'Before Sunrise', 'rating': 8.9},
        {'title': 'Howls Moving Castle', 'rating': 9.2},
        {'title': 'The Avengers', 'rating': 7.8},
        {'title': 'Life of Pi', 'rating': 8.7},
        {'title': 'Nope', 'rating': 8.9}     
    ]

    return render_template('list_all_movies.html', list_movies_active=True)


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
