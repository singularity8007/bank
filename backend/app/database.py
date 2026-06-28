import psycopg
from psycopg.rows import dict_row
from app.logging_config import logger

# Hardcoded for local learning project (not recommended for real projects)
DATABASE_URL = "postgresql://db_user:db%40user@localhost:5432/postgres?options=-csearch_path%3Dbank,public"


def get_connection():
    """Returns a new database connection"""
    try:
        conn = psycopg.connect(DATABASE_URL, row_factory=dict_row)
        return conn
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise