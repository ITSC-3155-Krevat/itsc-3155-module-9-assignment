from flask import Flask, redirect, render_template, request

app = Flask(__name__)

movies = []
next_movie_id = 1

@app.route('/')
def index():
    return render_template('index.html')

# feature save/ create (2) -- cindy
@app.route('/movies/new', methods=['GET', 'POST'])
def create_movies_form():
    global next_movie_id
    
    if request.method == 'POST':
        title = request.form.get('title')
        director = request.form.get('director')
        rating = request.form.get('rating')
        movie_id = next_movie_id
        next_movie_id += 1

        #test -- checks if movie exists already
        if any(movie['title'] == title and movie['director'] == director for movie in movies):
            error_message = "Movie already exists!"
            return render_template('create_movies_form.html', create_rating_active=True, error=error_message)
        
        #create a new movie
        new_movie = {'movie_id': movie_id, 'title': title, 'director': director, 'rating': rating}
        # add new movie to the list
        movies.append(new_movie)
        
        return redirect('/movies')
    
    else:
        return render_template('create_movies_form.html', create_rating_active=True, movie_id=next_movie_id)

@app.route('/movies')
def list_all_movies():
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
