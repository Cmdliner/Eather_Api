import os
from models.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URI = os.getenv('DATABASE_URI') 
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


