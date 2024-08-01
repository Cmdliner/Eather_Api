import uuid
from sqlalchemy import Column, String, Float, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Test(Base):
    __tablename__ = "tests"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(50), index=True, unique=True)
    description = Column(String(255))
    price  = Column(Float(4))

    