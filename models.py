from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base


class UserInDB(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, unique=True)
    hashed_password = Column(String)
    role = Column(Integer)


class FilmInDB(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    release_year = Column(Integer, index=True)


class ActorInDB(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    info = Column(String, index=True)


class FilmStaffInDB(Base):
    __tablename__ = 'film_staff'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    film_id = Column(ForeignKey('films.id'))
    actor_id = Column(ForeignKey('actors.id'))


class FavoriteFilmsInDB(Base):
    __tablename__ = 'favorite_films'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    film_id = Column(Integer, ForeignKey('films.id'))


class FavoriteActorsInDB(Base):
    __tablename__ = 'favorite_actors'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(ForeignKey('users.id'))
    actor_id = Column(ForeignKey('actors.id'))
