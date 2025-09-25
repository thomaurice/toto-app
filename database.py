from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from constants import DATA_FOLDER, DB_PATH
from structlog import get_logger

logger = get_logger()


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String, primary_key=True)


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
    Base.metadata.create_all(bind=engine)


def user_exists(username: str) -> bool:
    """Check if a user exists in the database."""
    with SessionLocal() as session:
        user = session.query(User).filter(User.username == username).first()
        return user is not None
