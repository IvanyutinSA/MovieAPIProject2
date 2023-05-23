from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import services
import dependencies
import models
import schemas

from database import engine


models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix='/actor',
    tags=['Actor | Common User']
)


@router.get('/', response_model=list[schemas.Actor])
def read_actors(
        db: Session = Depends(dependencies.get_db)
):
    return services.actors.get_actors(db)


@router.get('/{actor_id}', response_model=schemas.Actor)
def read_actor_by_id(
        actor_id: int,
        db: Session = Depends(dependencies.get_db)
):
    return services.actors.get_actor_by_id(db, actor_id)
