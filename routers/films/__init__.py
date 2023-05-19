from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from routers import auth
import crud
import dependencies
import models
import schemas

from . import common_users
from . import privileged_users

from database import engine

models.Base.metadata.create_all(bind=engine)