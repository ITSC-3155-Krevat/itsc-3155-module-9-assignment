from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()
movie_repository.create_movie('Spiderman', 'Ronni Elhadidy', 5)
movie = movie_repository.get_movie_by_title('Spiderman')
print(movie.movie_id)
if __name__ == "__main__":
    app.run(debug=True)

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
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
   
    movie = movie_repository.get_movie_by_id(movie_id)
    
    
    if not movie:
        return "Movie not found", 404
    
    
    return render_template('edit_movies_form.html', movie=movie)


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    title = request.form['title']
    director = request.form['director']
    rating = request.form.get('rating', type=int)
    
    updated_movie = {
        'title': title,
        'director': director,
        'rating': rating
    }
    
    movie_repository.update_movie(movie_id, updated_movie)
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass
