from flask import Flask, redirect, render_template, request
from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movies = []
next_movie_id = 1

movie_repository = get_movie_repository()

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    return render_template('list_all_movies.html', movies=movies)

# create/ save feature cindy
@app.post('/movies/new')
def create_movie():
    global next_movie_id

    title = request.form.get('title')
    director = request.form.get('director')
    rating = request.form.get('rating')

    # Check if the movie already exists -- test
    if any(movie['title'] == title and movie['director'] == director for movie in movies):
        error_message = "Movie already exists!"
        return render_template('create_movies_form.html', create_rating_active=True, error=error_message)

    # Create a new movie
    movie_id = next_movie_id
    next_movie_id += 1
    new_movie = {'movie_id': movie_id, 'title': title, 'director': director, 'rating': rating}
    movies.append(new_movie)

    return redirect('/movies')


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


# Varsha's search movie function
@app.get('/movies/search')
def search_movies_form():
    return render_template('search_movies.html', search_active=True)

# Varsha's search movie function
@app.post('/movies/search')
def search_movies():
    title = request.form.get('title')
    movies_found = [movie for movie in movies if movie['title'] == title]
    if movies_found:
        return render_template('search_movies.html', movies_found=movies_found, search_active=True)
    else:
        return render_template('search_movies.html', not_found=True, search_active=True)


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