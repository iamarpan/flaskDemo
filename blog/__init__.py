from flask import Flask, url_for, flash 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import  LoginManager
from blog.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'



def create_app(class_config=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from blog.users.routes import users
    from blog.main.routes import main
    from blog.posts.routes import posts

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    return app
