from datetime import datetime
from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str


class User(BaseModel):
    id: int
    username: str


class Comment(BaseModel):
    id: int
    book_id: int
    user_id: int
    content: str
    start_position: int
    end_position: int
    created_at: datetime
