import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv
import os
from app.logging_config import logger

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://db_user:db%40user@localhost:5432/postgres")

engine = create_engine(DATABASE_URL, echo=True)  # echo=True shows SQL (good for learning)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_connection():
    """Returns a new database connection"""
    try:
        conn = psycopg.connect(DATABASE_URL, row_factory=dict_row)
        return conn
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise
