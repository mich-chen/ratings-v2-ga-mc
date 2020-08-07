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


# Generating 10 random users, and for each user
# generating 10 random ratings. We will be getting a random
# movie by picking from the all_movies_in_db list.
# looping over 10 times for 10 users
for n in range(10):
    # Creating a unique email for each user
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    # create a user here
    user = crud.create_user(email=email, password=password)

    # create 10 ratings for the user
    for i in range(10):
        # pick random movie and score
        random_movie = choice(all_movies_in_db)
        random_score = randint(1,5)

        # Create our new rating from these random things
        rating = crud.create_rating(score=random_score, 
                                movie=random_movie,
                                user=user)









