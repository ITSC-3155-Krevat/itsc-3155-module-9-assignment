from flask import Flask, redirect, render_template, request, session

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)
app.secret_key = 'your_secret_key' 

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()

@app.get('/')
def index():
    return render_template('index.html')

# Cindy's save function
@app.route('/movies/new', methods=['GET', 'POST'])
def create_movies_form():
    if request.method == 'POST':
        title = request.form.get('title')
        director = request.form.get('director')
        rating = request.form.get('rating')

        # Check if the movie already exists -- our test
        if any(movie['title'] == title and movie['director'] == director for movie in session.get('movies', [])):
            error_message = "Movie already exists!"
            return render_template('create_movies_form.html', create_rating_active=True, error=error_message)
        
        # Create a new movie 
        new_movie = {'title': title, 'director': director, 'rating': rating}
        # Get the list of movies
        movies = session.get('movies', [])
        # Add new movie to the list of movies
        movies.append(new_movie)
        # Update the movies list
        session['movies'] = movies
        # Redirect to the list all movies page after creating a new movie
        return redirect('/movies')
    
    else:
        return render_template('create_movies_form.html', create_rating_active=True)

# Cindy's Save movie function
@app.post('/movies')
def create_movie():
    title = request.form.get('title')
    director = request.form.get('director')
    rating = request.form.get('rating')

    # Create a new movie 
    new_movie = {'title': title, 'director': director, 'rating': rating}
    # Get the list of movies
    movies = session.get('movies', [])
    # Add new movie to the list of movies
    movies.append(new_movie)
    # Update the movies list 
    session['movies'] = movies

    return redirect('/movies')

#Cindy's Save function
@app.get('/movies')
def list_all_movies():
    # Get the list of movies from session
    movies = session.get('movies', [])

    return render_template('list_all_movies.html', movies=movies)



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
