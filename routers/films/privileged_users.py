from . import *

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
    return crud.add_film(db, film)


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
    return crud.add_film_staff_actor(db, actor_id, film_id)


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
    return crud.delete_film(db, film_id)


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
    return crud.update_film(db, film_id, film)

