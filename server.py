"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash,
                    session, redirect)

# Importing from files we've made
from model import connect_to_db
import crud

# Throw errors for undefined variables in Jinja2
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def show_homepage():
    """Show the app's homepage"""
    return render_template('homepage.html')


@app.route('/movies')
def show_all_movies():
    """Show all movies in database"""
    all_movies = crud.get_all_movies()
    return render_template("all_movies.html", movies=all_movies)


@app.route('/movies/<movie_id>')
def show_movie_details(movie_id):
    movie = crud.get_movie_by_id(movie_id)
    return render_template("movie_details.html", movie=movie)


@app.route('/users')
def show_all_users():
    all_users = crud.get_all_users()
    return render_template('all_users.html', users=all_users)

@app.route('/users/<user_id>')
def show_user_profile(user_id):
    user = crud.get_user_by_id(user_id)
    return render_template("user_profile.html", user=user)


if __name__ == '__main__':
    # Connect to db first, then app can access it.
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
