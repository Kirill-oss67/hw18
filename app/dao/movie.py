from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, id):
        return self.session.query(Movie).get(id)

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year)

    def get_by_director(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id)

    def get_by_genre(self, genre):
        return self.session.query(Movie).filter(Movie.genre_id == genre)

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
