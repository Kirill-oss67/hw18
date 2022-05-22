from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class BooksView(Resource):
    def get(self):
        all_directors = director_dao.get_all()
        return directors_schema.dump(all_directors), 200


@director_ns.route('/<int:id>')
class BookView(Resource):
    def get(self, id):
        director = director_dao.get_one(id)
        return director_schema.dump(director), 200
