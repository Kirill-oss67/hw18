from flask import Flask
from flask_restx import Api

from app.config import Config
# from models import Review, Book
from app.setup_db import db

from dao.views.director import director_ns
from dao.views.genre import genre_ns
from dao.views.movie import movie_ns


# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


if __name__ == '__main__':
    app = create_app(Config())

    app.run(host="localhost", port=10001, debug=True)
