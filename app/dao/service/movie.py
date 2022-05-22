# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

# Пример
from app.dao.movie import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_one(self, id):
        return self.movie_dao.get_one(id)

    def get_by_year(self, year):
        return self.movie_dao.get_by_year(year)

    def get_by_genre(self, genre):
        return self.movie_dao.get_by_genre(genre)

    def get_by_director(self, director_id):
        return self.movie_dao.get_by_director(director_id)

    def get_all(self):
        return self.movie_dao.get_all()

    def create(self, data):
        self.movie_dao.create(data)

    def update(self, data):
        id = data.get('id')
        movie = self.get_one(id)
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')

        self.movie_dao.update(movie)

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

        self.movie_dao.update(movie)

    def delete(self, id):
        self.movie_dao.delete(id)
