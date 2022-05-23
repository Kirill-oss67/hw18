from flask_restx import Resource, Namespace
from app.dao.model.genre import GenreSchema
from app.implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:id>')
class GenreView(Resource):
    def get(self, id):
        genre = genre_service.get_one(id)
        return genre_schema.dump(genre), 200
