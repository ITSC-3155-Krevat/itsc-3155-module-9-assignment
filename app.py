from flask import Flask, redirect, render_template, request, abort

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()

movie_repository = {
    1: {"title": "Movie 1", "director": "Director 1", "rating": 4.5},
    2: {"title": "Movie 2", "director": "Director 2", "rating": 3.8}
}


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True, movies = movie_repository)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    movieName = request.form.get('name')
    movieDirector = request.form.get('director')
    movieRating = request.form.get('ratings')
    if not (movieName or movieDirector or movieRating):
        print("Please fill out all the fields")
        abort(400)

    # movieRating = float(request.form.get('ratings'))
    rating = float(movieRating)
    if rating < 0 or rating > 5:
        print("The movie rating should be between 0 to 5")
        abort(400) 
    
    movie_repository.create_movie(movieName, movieDirector, rating)
    
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

# @app.get('/movies/<int:movie_id>')
# def get_single_movie(movie_id: int):
#     # Fetch the movie from the repository using its ID
#     single_movie = movie_repository.get(movie_id)

#     if single_movie:
#         return render_template('get_single_movie.html', single_movie=single_movie, movie_id=movie_id)
#     else:
#         abort(404)

# # Route to edit a movie
# @app.get('/movies/<int:movie_id>/edit')
# def get_edit_movies_page(movie_id: int):
#     movie_to_edit = movie_repository.get(movie_id)

#     if movie_to_edit:
#         return render_template('edit_movies_form.html', movie=movie_to_edit)
#     else:
#         abort(404)

# if __name__ == '__main__':
#     app.run(debug=True)


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass
