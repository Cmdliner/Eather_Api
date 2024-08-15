import uuid
from datetime import datetime, UTC
from models.base import Base
from sqlalchemy import String, ForeignKey, Float, TEXT
from sqlalchemy.orm import relationship, Mapped, mapped_column


class Appointment(Base):
    __tablename__ = "appointments"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    duration: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    patient_complaints: Mapped[str] = mapped_column(TEXT)
    price_total: Mapped[float] = mapped_column(Float(36))

    user = relationship("User", back_populates="appointments")
    tests = relationship(
        "Test", secondary="appointment_tests", back_populates="appointments"
    )

    def __repr__(self):
        return f"Appointment<user_id=({self.user_id}), duration=({self.duration})>"
