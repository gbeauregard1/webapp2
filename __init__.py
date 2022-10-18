from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# i might not need the database stuff ?
# db - SQLAlchemy()
# DB_NAME = "database.db"

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'lunch'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    #from .views import views
    # from .auth import auth
    # from .authnew import authnew
    from .testing import testing

    #app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(testing, url_prefix='/')

    #below ill import all classses ,classmembertwo, genre, etc
    # from .models import castMemberOne
    

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database.')