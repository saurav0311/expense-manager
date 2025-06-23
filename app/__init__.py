from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

login_manager=LoginManager()
db=SQLAlchemy()
bcrypt=Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expenses.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key="secret"
   
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    login_manager.login_view="auth.login"

    from .auth_routes import auth
    from .routes import main    
    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix="/auth")
    with app.app_context():
        db.create_all()
    return app


