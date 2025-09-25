import sqlite3

from constants import DATA_FOLDER, DB_PATH
from structlog import get_logger

logger = get_logger()


def init_database():
    """Initialize the users database."""
    # Create data folder if it doesn't exist
    DATA_FOLDER.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        logger.info("Initializing database at", db_path=DB_PATH)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY
            )
        """)
        conn.commit()


def user_exists(username: str) -> bool:
    """Check if a user exists in the database."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
        return cursor.fetchone() is not None
