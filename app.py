from flask import Flask, redirect, render_template, request, url_for,abort

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()
movie_repository.create_movie("The Shawshank Redemption", "Frank Darabont", 3.2)
movie_repository.create_movie("The Godfather", "Francis Ford Coppola", 5.0)
movie_repository.create_movie("The Dark Knight", "Christopher Nolan", 4.3)
movie_repository.create_movie("Forrest Gump", "Robert Zemeckis", 4.5)



@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    list_movies_active = movie_repository.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=list_movies_active)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    title = request.form.get("moviename");
    director = request.form.get("directorname");
    rating = request.form.get("movierating");
    try: 
        movierating = int(rating)
    except:
        ValueError
    movie_repository.create_movie(title, director, rating);
    # After creating the movie in the database, we redirect to the list all movies page
    title = request.form.get("title")
    director = request.form.get("director")
    rating = int(request.form.get("rating"))
    movie_id = movie_repository.create_movie(title, director, rating)
    
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
# first get the movie by title
    # Somehow get the movie's rating
    # return that to the search_movies.html
    movie_search = request.args.get('movie-search') 
    if movie_search:
        movie_search_trim = movie_search.strip().lower()
        movie = movie_repository.get_movie_by_title(movie_search_trim)
        if movie is not None:
            rating = movie.rating
            movie_title = movie.title
        else:
            rating = -1
            movie_title = None
        return render_template('search_movies.html', search_active=True, rating=rating, movie_title=movie_title)
    else:
        return render_template('search_movies.html', search_active=True, rating=None, movie_title=None)


#End of Sang Vang's Methods for Feature 3
    

movie_repo = get_movie_repository()
@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # Retrieve movie details using the get_movie_by_id function
    movie = movie_repo.get_movie_by_id(movie_id)
    
    # Render the template with movie details
    return render_template('get_single_movie.html', movie=movie)


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    return render_template('edit_movies_form.html')


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    title = request.form['title']
    director = request.form['director']
    rating = request.form['rating']
    # Convert rating to an integer
    rating = int(rating)
    # return redirect(f'/movies/{movie_id}')
    try: 
        # Updating the movie in the repository
        movie_repository.update_movie(movie_id, title, director, rating)

        # Redirecting back to the single movie's page on successful update
        return redirect(url_for('get_single_movie', movie_id=movie_id))
    except ValueError as e:
        # Handling the case where the movie ID does not exist
        return str(e), 404


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass
