import uvicorn

from fastapi import FastAPI

from routers import users, films, actors, auth

description = """
## Users
Каждый пользователь имеет поле role\n
Если role=1 пользователь считается привелегирированным и может выполнять все запросы\n
Если же role=0 действия пользователя ограничены
"""

app = FastAPI(
    title='Movie API',
    description=description,
    version='1.0.0',
    contact={
            "name": "Иванютин С.А.\nФИТ-221",
            "email": "ivanyutin2004@gmail.com",
        },
)

app.include_router(users.common_users.router)
app.include_router(users.privileged_users.router)

app.include_router(films.common_users.router)
app.include_router(films.privileged_users.router)

app.include_router(actors.common_users.router)
app.include_router(actors.privileged_users.router)

app.include_router(auth.router)


if __name__ == '__main__':
    uvicorn.run(app)
