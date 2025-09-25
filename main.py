from functools import partial
import os
from pathlib import Path
from typing import Annotated, Sequence, cast
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, Request
from pydantic import BaseModel
import jwt

from constants import BOOKS_FOLDER
from database import init_database, user_exists, create_user, verify_user

load_env = partial(load_dotenv, verbose=True)


class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


app = FastAPI(on_startup=[load_env, init_database])


def _create_access_token(username: str) -> str:
    payload = {"user": username}
    return jwt.encode(payload, os.environ.get("JWT_SECRET_KEY"), algorithm="HS256")


def _get_current_user(request: Request) -> str:
    if not (auth_header := request.headers.get("Authorization")):
        raise HTTPException(status_code=401, detail="No token provided")

    bearer_token = auth_header.split(" ")
    if len(bearer_token) != 2 or bearer_token[0] != "Bearer":
        raise HTTPException(status_code=401, detail="Invalid token format")

    try:
        decoded = cast(
            dict,
            jwt.decode(
                bearer_token[1],
                os.environ.get("JWT_SECRET_KEY"),
                algorithms=["HS256"],
            ),
        )
        user = decoded.get("user")
        if not user_exists(user):
            raise HTTPException(status_code=403, detail="Invalid user")
        return user
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


@app.get("/books")
def get_books() -> Sequence[str]:
    return [f.name for f in BOOKS_FOLDER.iterdir() if f.is_file()]


@app.get("/books/{book_name:str}")
def get_book(book_name: str) -> Path:
    book_path = BOOKS_FOLDER / book_name
    if not book_path.exists() or not book_path.is_file():
        raise HTTPException(status_code=404, detail="Book not found")
    with open(book_path, "r") as f:
        return f.read()


@app.get("/")
async def read_root(current_user: Annotated[str, Depends(_get_current_user)]):
    return {"Hello": current_user}


@app.post("/register")
async def register_user(user_data: UserCreate):
    """Register a new user with username and password."""
    try:
        create_user(user_data.username, user_data.password)
        return {"message": "User created successfully"}
    except ValueError:
        raise HTTPException(status_code=409, detail="Username already exists")


@app.post("/login")
async def login_user(user_credentials: UserLogin) -> str:
    """Authenticate user and return JWT token."""
    if verify_user(user_credentials.username, user_credentials.password):
        access_token = _create_access_token(user_credentials.username)
        return access_token
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")
