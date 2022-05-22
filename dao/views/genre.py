from flask_restx import Resource, Namespace
from dao.model.genre import GenreSchema
genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genre_ns.route('/')
class BooksView(Resource):
    def get(self):
        all_genres = genre_dao.get_all()
        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:id>')
class BookView(Resource):
    def get(self, id):
        genre = genre_dao.get_one(id)
        return genre_schema.dump(genre), 200
