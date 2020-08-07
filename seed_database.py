"""Script to seed database!
Do all the boring work for us. Thanks python <3"""

# importing os and libraries
import os
import json
from random import choice, randint
from datetime import datetime

# importing files we made in this directory
import crud
import model
import server

# Dropping and creating the db (in case it was there before)
os.system('dropdb ratings')
os.system('createdb ratings')

# Connecting our db to our Flask app
model.connect_to_db(server.app)

# Creating our tables from classes inherited from db.model
model.db.create_all()

# Load data 
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Loop over movie_data and use each dict to create a movie 
# w/ crud.create_movie, then add each movie to a list
# Create empty list to store all movies we will make
all_movies_in_db = []

# Loop over movie_data
for movie in movie_data:
    # Getting the release date to be a datetime object
    release_date_string = movie['release_date']
    release_date_format = '%Y-%m-%d'
    release_date = datetime.strptime(release_date_string, release_date_format)

    # Getting the rest of the data abt the movie
    title = movie['title']
    overview = movie['overview']
    poster_path = movie['poster_path']

    # Create our movie object and add to the db
    db_movie = crud.create_movie(title=title,
                                overview=overview,
                                release_date=release_date,
                                poster_path=poster_path)
    # Add our new movie object to the list of overall movies
    all_movies_in_db.append(db_movie)









