from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
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
    tags=['User | Privileged User'],
)


@router.post('/', response_model=schemas.User)
def create_user(
        current_user: Annotated[
                    schemas.User,
                    Depends(auth.get_current_user)
                ],
        user: schemas.UserToCreate,
        db: Session = Depends(dependencies.get_db)
):
    if not current_user.role:
        raise HTTPException(status_code=403)
    user.password = auth.get_password_hash(user.password)
    return services.users.create_user(db=db, user=user)


@router.post('/{user_id}/favorite-films/')
def add_user_favorite_film(
        user_id: int,
        film_id: int,
        current_user: Annotated[
                    schemas.User,
                    Depends(auth.get_current_user)
                ],
        db: Session = Depends(dependencies.get_db),
):
    if not current_user.role:
        raise HTTPException(status_code=403)
    favorite_film = services.users.add_users_favorite_film(db, user_id, film_id)
    return favorite_film


@router.get('/{user_id}/favorite-films', response_model=list[schemas.Film])
def read_users_favorite_films(
        user_id: int,
        current_user: Annotated[
                    schemas.User,
                    Depends(auth.get_current_user)
                ],
        db: Session = Depends(dependencies.get_db),
):
    if not current_user.role:
        raise HTTPException(status_code=403)
    user = schemas.User.from_orm(services.users.get_user_by_id(db, user_id))
    return services.users.get_users_favorite_films(db, user)


@router.post('/{user_id}/favorite-actors')
def add_users_favorite_actor(
        user_id: int,
        actor_id: int,
        current_user: Annotated[
                    schemas.User,
                    Depends(auth.get_current_user)
                ],
        db: Session = Depends(dependencies.get_db),
):
    if not current_user.role:
        raise HTTPException(status_code=403)
    return services.users.add_users_favorite_actor(db, user_id, actor_id)


@router.get('/{user_id}/favorite-actors', response_model=list[schemas.Actor])
def read_users_favorite_actors(
        user_id: int,
        current_user: Annotated[
            schemas.User,
            Depends(auth.get_current_user)
        ],
        db: Session = Depends(dependencies.get_db),
):
    if not current_user.role:
        raise HTTPException(status_code=403)
    user = schemas.User.from_orm(services.users.get_user_by_id(db, user_id))
    return services.users.get_users_favorite_actors(db, user)
