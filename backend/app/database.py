from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://db_user:db%40user@localhost:5432/postgres")

engine = create_engine(DATABASE_URL, echo=True)  # echo=True shows SQL (good for learning)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base = declarative_base()

class Base(declarative_base()):
    """Base class for all SQLAlchemy models."""

    __abstract__ = True  # Prevents SQLAlchemy from creating a table for this class
    __table_args__ = {"schema": "bank"}
    



def get_db():
    """Dependency for FastAPI routes to get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
