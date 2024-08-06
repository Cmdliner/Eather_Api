import uuid
from .base import Base
from sqlalchemy import Column, ForeignKey, String, TEXT, TIMESTAMP, Float
from sqlalchemy.orm import relationship


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    patient_complaints = Column(TEXT, nullable=False)
    diagnosis = Column(TEXT, nullable=True)
    date = Column(TIMESTAMP(timezone=True))
    tests_price = Column(Float, nullable=False)

    user = relationship("User", back_populates="appointments")
    tests = relationship("Test", secondary="appointment_tests", back_populates="appointment")
