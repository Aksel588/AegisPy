# core/database.py
#
# This file sets up the database connection and ORM base for your application using SQLAlchemy.
#
# Usage:
#   - The engine is created using the DATABASE_URL from your config.
#   - SessionLocal provides a session factory for database operations.
#   - Base is the declarative base class for your ORM models.
#   - Import SessionLocal and Base in your models and services as needed.
#
# Example usage in a model:
#   from core.database import Base
#   class User(Base):
#       __tablename__ = 'users'
#       ...
#
# Example usage in a service:
#   from core.database import SessionLocal
#   db = SessionLocal()
#   ...
#   db.close()
#
"""
This file initializes the SQLAlchemy engine, session factory, and base class for ORM models.
Edit or extend as needed for your project's database needs.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config.settings import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()