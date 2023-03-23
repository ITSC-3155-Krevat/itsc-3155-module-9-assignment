from flask import Flask, redirect, render_template, abort, request
from src.models.movie import Movie

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


#Temp movie
movie_repository.create_movie('Interstellar', 'Christopher Nolan', 10)
movie_repository.create_movie('Inception', 'Christopher Nolan', 10)
movie_repository.create_movie('The Dark Knight', 'Christopher Nolan', 9)

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    all_movies = movie_repository.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, all_movies = all_movies)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.route('/movies/search')
def search_movies():
    
    # Get the movie title from the query string
    title = request.args.get('title')
    if title: 
        title = title.title()

    # If no title is provided, just render the search page
    if not title:
        return render_template('search_movies.html')

    # Check if the movie exists in the repository
    movie = movie_repository.get_movie_by_title(title)

    if movie:
        # If the movie exists, get its rating and render the search page with the result
        rating = movie.rating
        return render_template('search_movies.html', search_active=True, title=title, rating=rating)
    else:
        # If the movie doesn't exist, render the search page with an error message
        return render_template('search_movies.html', search_active=True, title=title, rating=None)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # Feature 4 #
    
    movie = movie_repository.get_movie_by_id(movie_id)
    return render_template('get_single_movie.html', movie=movie, movie_repository=movie_repository)

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


if __name__ == "__main__":
    
    app.run(debug=True)