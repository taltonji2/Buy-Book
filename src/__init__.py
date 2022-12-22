from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

login_manager = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    db = SQLAlchemy(app)
    Migrate(app,db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "users.login"

    from src.core.views import core
    from src.error_pages.handlers import error_pages
    app.register_blueprint(core)
    app.register_blueprint(error_pages)
    return app