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


@app.route('/movies')
def show_all_movies():
    """Show all movies in database"""
    all_movies = crud.get_all_movies()
    return render_template("all_movies.html", movies=all_movies)


@app.route('/movies/<movie_id>')
def show_movie_details(movie_id):
    movie = crud.get_movie_by_id(movie_id)
    return render_template("movie_details.html", movie=movie)

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

@app.route('/users/<user_id>')
def show_user_profile(user_id):
    user = crud.get_user_by_id(user_id)
    return render_template("user_profile.html", user=user)


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
        


@app.route('/logout')
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
