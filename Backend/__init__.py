from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'Scrape.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
app = Flask(__name__)

app.config.from_object(Config)

# Initialize the SQLAlchemy instance
db = SQLAlchemy(app)

# Import routes after initializing the app and db
from Backend import routes