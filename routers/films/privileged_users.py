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
    prefix='/film',
    tags=['Film | Privileged User'],
)


@router.post('/', response_model=schemas.Film)
def add_film(
        film: schemas.FilmToCreate,
        current_user: Annotated[
            schemas.User,
            Depends(auth.get_current_user)
        ],
        db: Session = Depends(dependencies.get_db),
):
    if not current_user.role:
        raise HTTPException(status_code=403)
    return services.films.add_film(db, film)


@router.post('/{film_id}/staff')
def add_film_staff(
        film_id: int,
        actor_id: int,
        current_user: Annotated[
            schemas.User,
            Depends(auth.get_current_user)
        ],
        db: Session = Depends(dependencies.get_db)
):
    if not current_user.role:
        raise HTTPException(status_code=403)
    return services.films.add_film_staff_actor(db, actor_id, film_id)


@router.delete('/{film_id}/staff')
def delete_film(
        film_id: int,
        current_user: Annotated[
            schemas.User,
            Depends(auth.get_current_user)
        ],
        db: Session = Depends(dependencies.get_db)
):
    if not current_user.role:
        raise HTTPException(status_code=403)
    return services.films.delete_film(db, film_id)


@router.put('/{film_id}')
def update_film(
        film_id: int,
        film: schemas.FilmToCreate,
        current_user: Annotated[
            schemas.User,
            Depends(auth.get_current_user)
        ],
        db: Session = Depends(dependencies.get_db)
):
    if not current_user.role:
        raise HTTPException(status_code=403)
    return services.films.update_film(db, film_id, film)

