# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service
from flask import request
from app.dao.model.movie import MovieSchema
from flask_restx import Resource, Namespace

from app.implemented import movie_service

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        year = request.args.get('year')
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        if genre_id:
            movies = movie_service.get_by_genre(genre_id)
            return movies_schema.dump(movies), 200
        elif director_id:
            movies = movie_service.get_by_director(director_id)
            return movies_schema.dump(movies), 200
        if year:
            movies = movie_service.get_by_year(year)
            return movies_schema.dump(movies), 200
        else:
            all_movies = movie_service.get_all()
            return movies_schema.dump(all_movies), 200

    def post(self):
        try:
            req_json = request.json
            movie_service.create(req_json)
            return "", 201
        except Exception:
            return 'задано неверное значение', 400


@movie_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id):
        movie = movie_service.get_one(id)
        return movie_schema.dump(movie), 200

    def put(self, id):
        try:
            req_json = request.json
            req_json['id'] = id
            movie_service.update(req_json)
            return "", 204
        except Exception:
            return 'задано неверное значение', 400

    def patch(self, id):
        try:
            req_json = request.json
            req_json['id'] = id
            movie_service.update_part(req_json)
            return '', 204
        except Exception:
            return 'задано неверное значение', 400

    def delete(self, id):
        try:
            movie_service.delete(id)
            return '', 204
        except Exception:
            return 'задано неверное значение'
