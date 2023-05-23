from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from routers import auth
import services
import dependencies
import models
import schemas

from database import engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix='/user',
    tags=['User | Common User'],
)


@router.get('/', response_model=list[schemas.User])
def read_users(db: Session = Depends(dependencies.get_db)):
    users = services.users.get_users(db)
    return users


@router.get('/me/favorite-films', response_model=list[schemas.Film])
def read_me(
        current_user: Annotated[
            schemas.User,
            Depends(auth.get_current_user)
        ],
        db: Session = Depends(dependencies.get_db),
):
    return services.users.get_users_favorite_films(db, current_user)


@router.post('/me/favorite-films/')
def add_my_favorite_film(
        film_id: int,
        current_user: Annotated[
                    schemas.User,
                    Depends(auth.get_current_user)
                ],
        db: Session = Depends(dependencies.get_db),
):
    user_id = current_user.id
    favorite_film = services.users.add_users_favorite_film(db, user_id, film_id)
    return favorite_film


@router.post('/me/favorite-actors')
def add_my_favorite_actor(
        actor_id: int,
        current_user: Annotated[
                    schemas.User,
                    Depends(auth.get_current_user)
                ],
        db: Session = Depends(dependencies.get_db),
):
    return services.users.add_users_favorite_actor(db, current_user.id, actor_id)


@router.get('/me/favorite-actors', response_model=list[schemas.Actor])
def read_my_favorite_actors(
        current_user: Annotated[
            schemas.User,
            Depends(auth.get_current_user)
        ],
        db: Session = Depends(dependencies.get_db),
):
    return services.users.get_users_favorite_actors(db, current_user)
