from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

from app.auth.routes import auth_bp
# …
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # init extensions…
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # register auth at /auth
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # register expenses (no prefix or add your own)
    from app.expenses.routes import exp_bp
    app.register_blueprint(exp_bp)

    return app
