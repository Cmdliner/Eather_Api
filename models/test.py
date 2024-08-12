import uuid
from .base import Base
from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship


class Test(Base):
    __tablename__ = "tests"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(50), index=True, unique=True, nullable=False)
    price = Column(Float(8), nullable=False)
    appointments = relationship('Appointment', secondary='appointment_tests', back_populates='tests')