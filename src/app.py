from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from decouple import config

config.encoding = 'cp1251'

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config('DATABASE_URL')

