from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager


# globally accessible variables
login = LoginManager()
mongodb = PyMongo()
db = SQLAlchemy()
migrate = Migrate()


# decorator registers the method with Flask-Login
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# db.Model is a base class for all models from Flask-SQLAlchemy
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return 'Username: {}'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Apod(db.Model):
    """ Astronomy Picture of the Day (APOD) """
    date = db.Column(db.String, primary_key=True)
    explanation = db.Column(db.String)
    media_type = db.Column(db.String)
    title = db.Column(db.String)
    url = db.Column(db.String)
    path = db.Column(db.String)

    def __repr__(self):
        return 'Astronomy Picture of the Day: {}'.format(self.title)


class Sol(db.Model):
    sol = db.Column(db.Integer, primary_key=True)
    average_temperature = db.Column(db.Float)
    high_temperature = db.Column(db.Float)
    low_temperature = db.Column(db.Float)
    horizontal_wind_speed = db.Column(db.Float)
    pressure = db.Column(db.Float)

    def __repr__(self):
        return 'sol: {}'.format(self.sol)


class Flare(db.Model):
    id = db.Column(db.String, primary_key=True)
    begin_time = db.Column(db.DateTime)
    peak_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    class_type = db.Column(db.String)
    activity_region = db.Column(db.String)

    def __repr__(self):
        return 'flare: {}'.format(self.id)