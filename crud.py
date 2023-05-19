import sqlalchemy
from sqlalchemy.orm import Session

import models
import schemas


def get_users(db: Session):
    return db.query(models.UserInDB).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.UserInDB).filter(
        models.UserInDB.id == user_id
    ).first()


def get_user_by_name(db: Session, username: str):
    return db.query(models.UserInDB).filter(
        models.UserInDB.name == username
    ).first()


def create_user(db: Session, user: schemas.UserToCreate):
    db_user = models.UserInDB(
        name=user.name,
        hashed_password=user.password,
        role=user.role,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def add_users_favorite_film(db: Session, user_id: int, film_id: int):
    db_favorite_film = models.FavoriteFilmsInDB(
        user_id=user_id,
        film_id=film_id,
    )
    db.add(db_favorite_film)
    db.commit()
    db.refresh(db_favorite_film)
    return db_favorite_film


def add_users_favorite_actor(db: Session, user_id: int, actor_id: int):
    db_favorite_actor = models.FavoriteActorsInDB(
        user_id=user_id,
        actor_id=actor_id,
    )
    db.add(db_favorite_actor)
    db.commit()
    db.refresh(db_favorite_actor)
    return db_favorite_actor


def add_film_staff_actor(db: Session, actor_id: int, film_id: int):
    db_film_actor = models.FilmStaffInDB(
        actor_id=actor_id,
        film_id=film_id,
    )
    db.add(db_film_actor)
    db.commit()
    db.refresh(db_film_actor)
    return db_film_actor


def add_film(db: Session, film: schemas.FilmToCreate):
    db_film = models.FilmInDB(
        name=film.name,
        description=film.description,
        release_year=film.release_year,
    )
    db.add(db_film)
    db.commit()
    db.refresh(db_film)
    return db_film


def get_users_favorite_films(db: Session, user: schemas.User):
    films_id = db.query(models.FavoriteFilmsInDB).filter(
        models.FavoriteFilmsInDB.user_id == user.id
    ).all()

    films_id = list(map(lambda x: x.film_id, films_id))

    films = db.query(models.FilmInDB).filter(
        models.FilmInDB.id.in_(films_id)
    ).all()

    return films


def get_users_favorite_actors(db: Session, user: schemas.User):
    actors_id = [x.actor_id for x in db.query(models.FavoriteActorsInDB).filter(
        models.FavoriteActorsInDB.user_id == user.id
    ).all()]

    actors = db.query(models.FilmInDB).filter(
        models.FilmInDB.id.in_(actors_id)
    ).all()

    return actors


def get_film_staff(db: Session, film_id: int):
    film_staff_id = [x.actor_id for x in db.query(models.FilmStaffInDB).filter(
        models.FilmStaffInDB.film_id == film_id
    ).all()]

    actors = db.query(models.ActorInDB).filter(
        models.ActorInDB.id.in_(film_staff_id)
    )

    return actors


def get_films_there_was_actor(db: Session, actor_id: int):
    films_id = [x.film_id for x in db.query(models.FilmStaffInDB).filter(
        models.FilmStaffInDB.actor_id == actor_id
    ).all()]

    films = db.query(models.FilmInDB).filter(
        models.FilmInDB.id.in_(films_id)
    ).all()

    return films


def get_films(db: Session):
    return db.query(models.FilmInDB).all()


def get_film_by_id(db: Session, film_id: int):
    return db.query(models.FilmInDB).filter(
        models.FilmInDB.id == film_id
    ).first()


def get_films_by_name(db: Session, film_name: str):
    return db.query(models.FilmInDB).filter(
        models.FilmInDB.name == film_name
    ).all()


def get_films_by_release_year(db: Session, year: int):
    return db.query(models.FilmInDB).filter(
        models.FilmInDB.release_year == year
    ).all()


def get_films_staff_by_id(db: Session, film_id: int):
    actors_id = db.query(models.FilmStaffInDB).filter(
        models.FilmStaffInDB.film_id == film_id
    )
    return db.query(models.ActorInDB).filter(
        models.ActorInDB.id in actors_id
    )


def add_actor(db: Session, actor: schemas.ActorToCreate):
    db_actor = models.ActorInDB(
        name=actor.name,
        info=actor.info,
    )

    db.add(db_actor)
    db.commit()
    db.refresh(db_actor)
    return db_actor


def get_actor_by_id(db: Session, actor_id: int):
    actor = db.query(models.ActorInDB).filter(
        models.ActorInDB.id == actor_id
    ).first()
    return actor


def add_actors_film(db: Session, actor_id: int, film_id: int):
    db_film_staff = models.FilmStaffInDB(
        actor_id=actor_id,
        film_id=film_id,
    )

    db.add(db_film_staff)
    db.commit()
    db.refresh(db_film_staff)

    return db_film_staff


def get_actors(db: Session):
    return db.query(models.ActorInDB).all()


def update_actor(db: Session, actor_id: int, new_actor: schemas.ActorToCreate):
    actor = get_actor_by_id(db, actor_id)
    actor.name = new_actor.name
    actor.info = new_actor.info
    db.commit()
    db.refresh(actor)
    return actor


def delete_actor(db: Session, actor_id: int):
    actor = db.query(models.ActorInDB).filter(
        models.ActorInDB.id == actor_id
    ).first()

    db.delete(actor)
    db.commit()
    return 'ok'


def update_film(db: Session, film_id: int, new_film: schemas.FilmToCreate):
    film = get_film_by_id(db, film_id)
    film.name = new_film.name
    film.description = new_film.description
    film.release_year = new_film.release_year
    db.commit()
    db.refresh(film)
    return film


def delete_film(db: Session, film_id: int):
    actor = get_film_by_id(db, film_id)
    db.delete(actor)
    db.commit()
    return 'ok'


