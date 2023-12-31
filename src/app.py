from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.auth.users import auth_backend, fastapi_users
from src.schemas.users import UserCreate, UserRead, UserUpdate
from src.routes.posts import router as posts
from src.routes.likes import router as likes
from src.routes.dislikes import router as dislike
from src.routes.celery_worker import router as worker

app = FastAPI(title="Ray_test_project")


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

app.include_router(posts)

app.include_router(likes)

app.include_router(dislike)

app.include_router(worker)
