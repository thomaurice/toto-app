from functools import partial
import os
from pathlib import Path
from typing import Annotated, Sequence, cast
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, Request
from pydantic import BaseModel
import jwt

from constants import BOOKS_FOLDER
from database import UserAlreadyExists, init_database, create_user, verify_user
import database
from domain_models import Book, User

load_env = partial(load_dotenv, verbose=True)


class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


app = FastAPI(
    title="Toto App API",
    description="API for managing books and user comments",
    version="0.1.0",
    on_startup=[load_env, init_database],
)


def _create_access_token(username: str) -> str:
    payload = {"user": username}
    return jwt.encode(payload, os.environ.get("JWT_SECRET_KEY"), algorithm="HS256")


def _get_current_user(request: Request) -> User:
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
        username = decoded.get("user")
        user = database.get_user_by_username(username)
        if not user:
            raise HTTPException(status_code=403, detail="Invalid user")
        return user
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


@app.get("/books", operation_id="get_books")
def get_books() -> Sequence[Book]:
    return database.get_books()


@app.get("/books/{book_id:int}/content", operation_id="get_book")
def get_book(book_id: int) -> Path:
    book = database.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book_path = BOOKS_FOLDER / f"{book.title}.txt"
    if not book_path.exists() or not book_path.is_file():
        raise HTTPException(status_code=404, detail="Book not found")
    with open(book_path, "r") as f:
        return f.read()


class CommentCreate(BaseModel):
    content: str
    start_position: int
    end_position: int


@app.post("/books/{book_id:int}/comments", operation_id="create_comment")
async def create_comment(
    book_id: int,
    comment_data: CommentCreate,
    current_user: Annotated[User, Depends(_get_current_user)],
):
    database.add_comment(
        book_id=book_id,
        user_id=current_user.id,
        content=comment_data.content,
        start_position=comment_data.start_position,
        end_position=comment_data.end_position,
    )
    return {"message": "Comment added successfully"}


@app.get("/books/{book_id:int}/comments", operation_id="get_book_comments")
async def get_book_comments(
    book_id: int,
):
    return database.get_book_comments(book_id)


@app.post("/register", operation_id="register_user")
async def register_user(user_data: UserCreate):
    """Register a new user with username and password."""
    try:
        create_user(user_data.username, user_data.password)
        return {"message": "User created successfully"}
    except UserAlreadyExists as e:
        raise HTTPException(status_code=409, detail="Username already exists") from e


@app.post("/login", operation_id="login_user")
async def login_user(user_credentials: UserLogin) -> str:
    """Authenticate user and return JWT token."""
    if verify_user(user_credentials.username, user_credentials.password):
        access_token = _create_access_token(user_credentials.username)
        return access_token
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")
