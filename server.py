"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash,
                    session, redirect)
from flask_debugtoolbar import DebugToolbarExtension

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


@app.route('/movies', methods=['GET', 'POST'])
def handle_all_movies():
    """Show all movies in database or create a movie"""
    if request.method == 'GET':
        all_movies = crud.get_all_movies()
        return render_template("all_movies.html", movies=all_movies)

    elif request.method == 'POST':
        title = request.form.get('title')
        overview = request.form.get('overview')
        release_date = request.form.get('release_date')
        poster_path = request.form.get('poster_path')
        crud.create_movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)
        all_movies = crud.get_all_movies()
        return render_template("all_movies.html", movies=all_movies)


@app.route('/movies/<movie_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_single_movie(movie_id):
    if request.method == 'GET':
        movie = crud.get_movie_by_id(movie_id)
        return render_template("movie_details.html", movie=movie)

    elif request.method == 'PUT':
        # TODO: add CRUD function to update movie (if want)

    elif request.method == 'DELETE':
        # TODO: add CRUD function to delete movie (if want feature)

@app.route('/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'GET':
        all_users = crud.get_all_user()
        return render_template('all_users.html', users=all_users)

    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = crud.get_user_by_email(email)

        if user:
            flash('You cannot create an account with that email. Try again.')
        else:
            crud.create_user(email=email, password=password)
            flash('Account created successfully!')
        return redirect('/')

@app.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_single_user(user_id):
    if request.method == 'GET':
        user = crud.get_user_by_id(user_id)
        return render_template("user_profile.html", user=user)
    
    elif request.method == 'PUT':
        # TODO: add CRUD function to update/modify user details
        # crud.update_user(user_id)
    
    elif request.method == 'DELETE':
        # TODO: add CRUD function to delete user
        # crud.delete_user(user_id)

@app.route('/login', methods=['POST'])
def process_login():
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user and password == user.password:
        session['user_id']= user.user_id
        flash('Logged in!')
    else:
        
        flash('Incorrect password or email. Try again.')

    return redirect('/')
        


@app.route('/logout', methods=['DELETE'])
def process_logout():
    # Deletes user from session to log them out
    del session['user_id']
    
    return redirect('/')






if __name__ == '__main__':
    # Connect to db first, then app can access it.
    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(host='0.0.0.0')
