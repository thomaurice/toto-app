import bcrypt
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
    password_hash: Mapped[str] = mapped_column(String, nullable=False)


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


def user_exists(username: str) -> bool:
    """Check if a user exists in the database."""
    with SessionLocal() as session:
        user = session.query(User).filter(User.username == username).first()
        return user is not None


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
