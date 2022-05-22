from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, id):
        return self.session.query(Movie).get(id)

    def get_all(self):
        return self.session.query(Movie).all()

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, id):
        movie = self.get_one(id)
        self.session.delete(movie)
        self.session.commit()
