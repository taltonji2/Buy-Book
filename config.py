from os import environ
from dotenv import load_dotenv

load_dotenv()

class Config:
    FLASK_APP = 'wsgi.py'
    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
   
    CONNECTION = "mysql+pymysql://{0}:{1}@{2}/{3}".format(environ.get('DBUSER'), environ.get('DBPASS'), environ.get('DBHOST'), environ.get('DBNAME'))
    SQLALCHEMY_DATABASE_URI = CONNECTION
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
