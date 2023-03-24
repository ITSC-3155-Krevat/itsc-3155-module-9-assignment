from flask import Flask, redirect, request, render_template

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
    movies = []
    movies.append(movie_repository.get_all_movies)

    return render_template('list_all_movies.html', list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    movie_name = request.form.get('movie-name', type = str)
    movie_director = request.form.get('movie-director', type = str)
    movie_ranking = request.form.get('rating', type = int)
    movie_repository.create_movie(movie_name, movie_director, movie_ranking)
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.route('/movies/search', methods=['GET', 'POST'])
def search_movies():
    # TODO: Feature 3
    if (request.method == "GET"):
        request_name = request.args.get('movie-name')
        movie_name = movie_repository.get_movie_by_title(request_name)
        if (movie_name != None):
            return render_template('search_movies.html', search_active=True, movie=movie_name, title=movie_name.title, rating=movie_name.rating)
        else:
            return render_template('search_movies.html', search_active=True)
    else:
        request_name = request.form.get('movie-name')
        movie_name = movie_repository.get_movie_by_title(request_name)
        if (movie_name != None):
            return render_template('search_movies.html', search_active=True, movie=movie_name, title=movie_name.title, rating=movie_name.rating)
        else:
            return render_template('search_movies.html', search_active=True)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    return render_template('get_single_movie.html')



@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    # Obtains movie in the database by ID
    movie = movie_repository.get_movie_by_id(movie_id)
    return render_template('edit_movies_form.html', movie=movie)


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    # Pulls the title, director, rating and then updates
    title = request.form['title']
    director = request.form['director']
    rating = int(request.form['rating'])
    movie_repository.update_movie(movie_id, title, director, rating)
    # Updates the movie within the database, then redirect towards to the page
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass
