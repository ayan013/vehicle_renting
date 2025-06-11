from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# This file is responsible for creating database, session and declaring Base class
DATABASE_URL="sqlite:///./rental.db"

engine= create_engine(DATABASE_URL,connect_args={"check same thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

