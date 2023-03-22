from flask import Flask, redirect, render_template , request
#

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
    
    #get dict from get_all_movies
    all_movies = movie_repository.get_all_movies()
   
    return render_template('list_all_movies.html', list_movies_active=True, all_movies = all_movies)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    movie_name = request.form['movieName']
    director_name = request.form['directorName']
    rating = request.form['selectRating']
    get_movie_repository().create_movie(movie_name, director_name, int(rating))
    print(movie_name, director_name, int(rating))
    # After creating the movie in the database, we redirect to the list all movies page
    movie_name = request.form['movieName']
    director_name = request.form['directorName']
    rating = request.form['selectRating']
    get_movie_repository().create_movie(movie_name, director_name, int(rating))
    print(movie_name, director_name, int(rating))
    print(movie_repository.get_all_movies())
    
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # Feature 3
    title = request.args.get("title") # request.args returns ImmutableMultiDict
    #print(title) # Use .get("title") to get the user input
    if (title): #If there is a title (any user input)
        rating = movie_repository.get_movie_by_title(title).rating # Returns None if there is no match
        if (rating): #If there was a match then rating != None
            return render_template('search_movies.html', title=title, rating=rating, search_active = True)
    #else:
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
