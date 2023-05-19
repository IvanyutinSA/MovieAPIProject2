import uvicorn

from fastapi import FastAPI

from routers import users, films, actors, auth
import routers
print(routers.users.common_users.router)

app = FastAPI()

app.include_router(users.privileged_users.router)
app.include_router(users.common_users.router)
app.include_router(films.privileged_users.router)
app.include_router(films.common_users.router)
app.include_router(actors.privileged_users.router)
app.include_router(actors.common_users.router)
app.include_router(auth.router)


if __name__ == '__main__':
    uvicorn.run(app)
