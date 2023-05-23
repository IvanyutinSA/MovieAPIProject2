from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import services
import dependencies
import models
import schemas

from database import engine

models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix='/film',
    tags=['Film | Common User'],
)


@router.get('/', response_model=list[schemas.Film])
def read_films(db: Session = Depends(dependencies.get_db)):
    films = services.films.get_films(db)
    return films


@router.get('/{film_id}', response_model=schemas.Film)
def read_film_by_id(
        film_id: int,
        db: Session = Depends(dependencies.get_db)
):
    return services.films.get_film_by_id(db, film_id)


@router.get('/{film_name}', response_model=list[schemas.Film])
def read_films_by_name(
        film_name: str,
        db: Session = Depends(dependencies.get_db)
):
    films = services.films.get_films_by_name(db, film_name)
    return films


@router.get('/{film_id}/staff', response_model=list[schemas.Actor])
def read_films_staff(
        film_id: int,
        db: Session = Depends(dependencies.get_db)
):
    return services.films.get_films_staff_by_id(db, film_id)


@router.get('/year/{year}', response_model=list[schemas.Film])
def read_films_by_release_year(
        year: int,
        db: Session = Depends(dependencies.get_db),
):
    return services.films.get_films_by_release_year(db, year)
