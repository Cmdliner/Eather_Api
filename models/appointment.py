import uuid
from datetime import datetime, UTC
from .base import Base
from sqlalchemy import Column, String, TIMESTAMP, TEXT, ForeignKey, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column


class Appointment(Base):
    __tablename__ = "appointments"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"))
    duration: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False, default=lambda: datetime.now(UTC)
    )
    patient_complaints: Mapped[str] = mapped_column(TEXT, nullable=False)
    price_total: Mapped[float] = mapped_column(Float(36), nullable=False)

    user = relationship("User", back_populates="appointments")
    tests = relationship("Test", secondary="appointment_tests", back_populates="appointment")
