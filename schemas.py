from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserBase(BaseModel):
    name: str
    role: int


class UserToCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    hashed_password: str

    class Config:
        orm_mode = True


class FilmBase(BaseModel):
    name: str
    description: str
    release_year: int


class FilmToCreate(FilmBase):
    pass


class Film(FilmBase):
    id: int

    class Config:
        orm_mode = True


class ActorBase(BaseModel):
    name: str
    info: str


class ActorToCreate(ActorBase):
    pass


class Actor(ActorBase):
    id: int

    class Config:
        orm_mode = True
