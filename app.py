from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()
movie_repository.create_movie("The movie", "Keanu Reeves", 4)

# sample movie to be taken out later
movie_repository.create_movie('The Matrix', 'The Wachowski Brothers', 5)


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1 [DONE]
    return render_template('list_all_movies.html', list_movies_active=True, movies=movie_repository.get_all_movies())


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2 [DONE]
    # After creating the movie in the database, we redirect to the list all movies page
    title = request.form.get('title') or None
    director = request.form.get('director') or None
    rating = int(request.form.get('rating', 0))
    if title != None and director != None and rating >= 0 and rating <= 5:
        movie_repository.create_movie(title, director, rating)
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3 [DONE]
    movie = None
    #get the form data
    search_movie = request.args.get('form_search')
    if movie_repository.get_movie_by_title(search_movie):
        movie = movie_repository.get_movie_by_title(search_movie)
        return render_template('search_movies.html', search_active=True, movie=movie)
    elif search_movie == None:
        return render_template('search_movies.html', search_active=False, movie=movie)
    else:
        return render_template('search_movies.html', search_active=True, movie=None)

@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4 
    movie = movie_repository.get_movie_by_id(movie_id)
    return render_template('get_single_movie.html', movie=movie)


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    return render_template('edit_movies_form.html', movie=movie_repository.get_movie_by_id(movie_id))


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    title = request.form.get('title') or None
    director = request.form.get('director') or None
    rating = int(request.form.get('rating', 0))
    if title != None and director != None and rating >= 0 and rating <= 5:
        movie_repository.update_movie(movie_id,title,director,rating)
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass
