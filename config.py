from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    FLASK_APP = 'wsgi.py'
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_ENV = environ.get('FLASK_ENV')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
   
    CONNECTION = "mysql+pymysql://{0}:{1}@{2}/{3}".format(environ.get('DBUSER'), environ.get('DBPASS'), environ.get('DBHOST'), environ.get('DBNAME'))
    SQLALCHEMY_DATABASE_URI = CONNECTION
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get('DEV_DATABASE_URI')