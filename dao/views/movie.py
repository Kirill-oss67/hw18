# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service
from flask import request
from dao.model.movie import MovieSchema
from flask_restx import Resource, Namespace

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
movie_ns = Namespace('movies')


@movie_ns.route('/')
class BooksView(Resource):
    def get(self):
        all_movies = movie_dao.get_all()
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movie_dao.create(req_json)

        return "", 201


@movie_ns.route('/<int:id>')
class BookView(Resource):
    def get(self, id):
        movie = movie_dao.get_one(id)
        return movie_schema.dump(movie), 200

    def put(self, id):
        req_json = request.json
        req_json['id'] = id
        movie_dao.update(req_json)

        return "", 204

    def putch(self, id):
        req_json = request.json
        req_json['id'] = id
        movie_dao.update_part(req_json)

        return '', 204

    def delete(self, id):
        movie_dao.delete(id)
        return '', 204
