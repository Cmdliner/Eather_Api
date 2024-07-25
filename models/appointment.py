import uuid
from config.db import Base
from sqlalchemy import Column, ForeignKey, String, Text, Table
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func


appointment_tests = Table(
    "appointment_tests",
    Base.metadata,
    Column("appointment_id", UUID(as_uuid=True), ForeignKey("appointments.id")),
    Column("test_id", UUID(as_uuid=True), ForeignKey("tests.id")),
)


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    created_at = Column(String, server_default=func.now())
    symptoms = Column(Text)

    user = relationship("User", back_populates="appointments")
    recommended_tests = relationship(
        "Test", secondary=appointment_tests, back_populates="appointment"
    )
    payment = relationship("Payment", back_populates="appointments", uselist=False)
