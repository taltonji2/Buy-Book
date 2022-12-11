from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, BooleanField
import my_secrets
import pymysql
import sys


conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(my_secrets.dbuser, my_secrets.dbpass, my_secrets.dbhost, my_secrets.dbname)
login_manager = LoginManager()

def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)
    app.config["SECRET_KEY"] = "SuperSecretKey"
    app.config["SQLALCHEMY_DATABASE_URI"] = conn
    db = SQLAlchemy(app)
    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes

        # Register Blueprints
        app.register_blueprint(routes.main_bp)


        return app