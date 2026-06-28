import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv
import os
from app.logging_config import logger

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    """Get a new database connection"""
    try:
        conn = psycopg.connect(DATABASE_URL, row_factory=dict_row)
        return conn
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise