"""
The code is setting up SQLAlchemy so your FastAPI app can talk to Postgres.
SQLAlchemy is an Object Relational Mapper (ORM) allows us to make python's 
objects and classes to database tables and entries.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

DATABASE_URL = "postgresql://admin:password@db:5432/pharm_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    line = Column(String, nullable=False)
