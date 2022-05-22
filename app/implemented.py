# файл для создания DAO и сервисов чтобы импортировать их везде
from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.service.director import DirectorService
from app.dao.service.genre import GenreService
from app.dao.movie import MovieDAO
from app.dao.service.movie import MovieService
from app.setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)
