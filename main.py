from functools import partial
import os
from pathlib import Path
from typing import Annotated, Sequence, cast
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, Request
import jwt

load_env = partial(load_dotenv, verbose=True)


app = FastAPI(on_startup=[load_env])
USERS = {"TOTO"}
DATA_FOLDER = Path("./local-data")
BOOKS_FOLDER = DATA_FOLDER / "books"


def get_current_user(request: Request) -> str:
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
        if user not in USERS:
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
async def read_root(current_user: Annotated[str, Depends(get_current_user)]):
    return {"Hello": current_user}
