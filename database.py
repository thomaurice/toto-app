from typing import Sequence
import bcrypt
from sqlalchemy import create_engine, delete, insert
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from constants import BOOKS_FOLDER, DATA_FOLDER, DB_PATH
from structlog import get_logger

import domain_models

logger = get_logger()


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str] = mapped_column()


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column()
    user_id: Mapped[int] = mapped_column()
    content: Mapped[str] = mapped_column()
    start_position: Mapped[int] = mapped_column()
    end_position: Mapped[int] = mapped_column()


# Create the SQLAlchemy engine
engine = create_engine(f"sqlite:///{DB_PATH}")

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)


def init_database():
    """Initialize the users database."""
    # Create data folder if it doesn't exist
    DATA_FOLDER.mkdir(parents=True, exist_ok=True)

    # Create all tables
    logger.info("Initializing database at", db_path=DB_PATH)
    Base.metadata.create_all(bind=engine, checkfirst=True)

    _sync_books()


def _sync_books():
    """Sync the books in the database with the text files in the books folder."""
    with SessionLocal.begin() as session:
        books = [
            Book(title=f.stem)
            for f in BOOKS_FOLDER.iterdir()
            if f.is_file() and f.suffix == ".txt"
        ]
        session.execute(
            delete(Book).where(Book.title.not_in([book.title for book in books]))
        )
        session.execute(
            insert(Book)
            .prefix_with("OR IGNORE")
            .values([{"title": book.title} for book in books])
        )
        logger.info(
            "📚 Synced books in database with files in", books_folder=BOOKS_FOLDER
        )


def add_comment(
    book_id: int, user_id: int, content: str, start_position: int, end_position: int
) -> None:
    """Add a comment to a book by a user."""
    with SessionLocal.begin() as session:
        new_comment = Comment(
            book_id=book_id,
            user_id=user_id,
            content=content,
            start_position=start_position,
            end_position=end_position,
        )
        session.add(new_comment)
        session.commit()


def get_book_comments(book_id: int) -> Sequence[domain_models.Comment]:
    """Retrieve all comments for a given book."""
    with SessionLocal() as session:
        comments = session.query(Comment).filter(Comment.book_id == book_id).all()
        return [
            domain_models.Comment(
                id=comment.id,
                book_id=comment.book_id,
                user_id=comment.user_id,
                content=comment.content,
                start_position=comment.start_position,
                end_position=comment.end_position,
            )
            for comment in comments
        ]


def get_user_by_username(username: str) -> domain_models.User | None:
    """Check if a user exists in the database."""
    with SessionLocal() as session:
        user = session.query(User).filter(User.username == username).first()
        if not user:
            return None
        return domain_models.User(id=user.id, username=user.username)


def create_user(username: str, password: str) -> None:
    """Create a new user with hashed password. Returns True if successful, False if user already exists."""
    with SessionLocal() as session:
        # Check if user already exists
        existing_user = session.query(User).filter(User.username == username).first()
        if existing_user:
            raise ValueError("Username already exists")

        # Hash the password and create new user
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")
        new_user = User(username=username, password_hash=password_hash)
        session.add(new_user)
        session.commit()
        logger.info("Created new user", username=username)


def verify_user(username: str, password: str) -> bool:
    """Verify user credentials. Returns True if valid, False otherwise."""
    with SessionLocal() as session:
        user = session.query(User).filter(User.username == username).first()
        if not user:
            return False

        # Verify password against hash
        return bcrypt.checkpw(
            password.encode("utf-8"), user.password_hash.encode("utf-8")
        )


def get_books() -> list[str]:
    """Retrieve a list of all book titles in the database."""
    with SessionLocal() as session:
        books = session.query(Book).all()
        return [domain_models.Book(id=book.id, title=book.title) for book in books]


def get_book(book_id: int) -> domain_models.Book | None:
    """Retrieve a book by its ID."""
    with SessionLocal() as session:
        book = session.get(Book, book_id)
        if not book:
            return None
        return domain_models.Book(id=book.id, title=book.title)
