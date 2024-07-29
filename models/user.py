import uuid
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4))
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)

