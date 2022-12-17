from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()

def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    db = SQLAlchemy(app)
    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Import parts of our application
        from src.routes.index import index_bp

        # Register Blueprints
        app.register_blueprint(index_bp)

        return app