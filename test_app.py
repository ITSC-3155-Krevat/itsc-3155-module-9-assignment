from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()



@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    movie = movie_repository.get_movie_by_id(movie_id)
    return render_template('get_single_movie.html', movie = movie)