class MovieRepository:

    def get_all_movies(self):
        # TODO get all movies from the DB

        from app import db
        from app.models import Movie

        class MovieRepository:
            def get_all_movies(self):
                return db.session.query(Movie).all()
                return None

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        from app import db
        from app.models import Movie

        class MovieRepository:
            def get_movie_by_id(self, movie_id):
                return db.session.query(Movie).filter_by(movie_id=movie_id).first()
                return None

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        from app import db
        from app.models import Movie

        class MovieRepository:
            def create_movie(self, title, director, rating):
                new_movie = Movie(title=title, director=director, rating=rating)
                db.session.add(new_movie)
                db.session.commit()
                return new_movie
                return None

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        from app import db
        from app

        return None


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
