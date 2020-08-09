"""CRUD Operations!
Create, Read, Update, Delete"""

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_all_users():
    return db.session.query(User).all()

def get_user_by_id(id_num):
    return db.session.query(User).get(id_num)

def get_user_by_email(email):
    return db.session.query(User).filter_by(email=email).first()


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie


def get_all_movies():
    return db.session.query(Movie).all()


def get_movie_by_id(id_num):
    return Movie.query.get(id_num)
    # Could also do:
    #return db.session.query(Movie).fitler_by(movie_id=id_num).one()



def create_rating(score, movie, user):
    """Create and return a new rating."""

    rating = Rating(score=score, movie=movie,user=user)

    db.session.add(rating)
    db.session.commit()

    return rating




if __name__ == '__main__':
    from server import app
    connect_to_db(app)