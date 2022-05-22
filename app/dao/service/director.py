from app.dao.director import DirectorDAO


class DirectorService:

    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_one(self, id):
        return self.director_dao.get_one(id)

    def get_all(self):
        return self.director_dao.get_all()
