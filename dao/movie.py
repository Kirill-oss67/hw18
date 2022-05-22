from dao.model.movie import Movie


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

    def update(self, data):
        id = data.get('id')
        movie = self.get_one(id)
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        self.session.add(movie)
        self.session.commit()
        return  movie

    def update_part(self, data):
        id = data.get('id')
        movie = self.get_one(id)
        if 'title' in data:
            movie.title = data.get('title')
        if 'description' in data:
            movie.description = data.get('description')
        if 'trailer' in data:
            movie.trailer = data.get('trailer')
        if 'year' in data:
            movie.year = data.get('year')
        if 'rating' in data:
            movie.rating = data.get('rating')
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, id):
        movie = self.get_one(id)
        self.session.delete(movie)
        self.session.commit()
