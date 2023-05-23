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
    prefix='/actor',
    tags=['Actor | Privileged User']
)


@router.post('/', response_model=schemas.Actor)
def add_actor(
        actor: schemas.ActorToCreate,
        current_user: Annotated[
            schemas.User,
            Depends(auth.get_current_user)
        ],
        db: Session = Depends(dependencies.get_db)
):
    if not current_user.role:
        raise HTTPException(status_code=403)
    return services.actors.add_actor(db, actor)


@router.post('/{actor_id}/films')
def add_actors_film(
        actor_id: int,
        film_id: int,
        current_user: Annotated[
            schemas.User,
            Depends(auth.get_current_user)
        ],
        db: Session = Depends(dependencies.get_db)
):
    if not current_user.role:
        raise HTTPException(status_code=403)
    return services.actors.add_actors_film(db, actor_id, film_id)


@router.put('/{actor_id}')
def update_actor(
        actor_id: int,
        actor: schemas.ActorToCreate,
        current_user: Annotated[
            schemas.User,
            Depends(auth.get_current_user)
        ],
        db: Session = Depends(dependencies.get_db)
):
    if not current_user.role:
        raise HTTPException(status_code=403)
    return services.actors.update_actor(db, actor_id, actor)


@router.delete('/{actor_id}')
def delete_actor(
        actor_id: int,
        current_user: Annotated[
            schemas.User,
            Depends(auth.get_current_user)
        ],
        db: Session = Depends(dependencies.get_db)
):
    if not current_user.role:
        raise HTTPException(status_code=403)
    return services.actors.delete_actor(db, actor_id)
