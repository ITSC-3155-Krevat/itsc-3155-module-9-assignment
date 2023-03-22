from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    data = []

    for key in movie_repository.get_all_movies():
        if(movie_repository.get_movie_by_title(movie_repository.get_movie_by_id(key).title) not in data):
            data.append(movie_repository.get_movie_by_id(key))

    table_headings = ("Title","Director","Rating")

    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True,data=data,table_headings=table_headings)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    dir_name = str(request.form.get("dir"))
    movie_name = str(request.form.get("mname"))

    if (len(movie_name) == 0 or len(dir_name) == 0):
        return redirect('/movies')

    match str(request.form.get("rating")):
        case "1":
            movie_rating = 1
        case "2":
            movie_rating = 2
        case "3":
            movie_rating = 3
        case "4":
            movie_rating = 4
        case "5":
            movie_rating = 5
        case _:
            return redirect('/movies')
    movie_name = movie_name.title()
    dir_name = dir_name.title()
    # After creating the movie in the database, we redirect to the list all movies page
    movie_repository.create_movie(movie_name, dir_name, movie_rating)
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    title = request.form.get('title', '', type=str)
    movie = movie_repository.get_movie_by_title(title)
    if movie == title:
        movie_id = movie_repository.get_movie_by_id(movie)
        return render_template('get_single_movie.html', movie_id = movie_id)
    elif movie == None:
        return render_template('search_movies.html', search_active=True)
    else:
        return render_template('index.html')

@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    movie = movie_repository.get_movie_by_id(movie_id)
    
    return render_template('get_single_movie.html', movie=movie)


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    movie = movie_repository.get_movie_by_id(movie_id)

    return render_template('edit_movies_form.html', movie=movie)


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass


