import uuid
from config.db import Base
from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID


class Payment(Base):
    __tablename__ = "payments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    appointment_id = Column(
        UUID(as_uuid=True), ForeignKey("appointments.id"), nullable=False
    )
    amount = Column(Float, nullable=False)
    status = Column(String, default="unpaid")  # Paid, Unpaid, Pending

    relationship("Appointment", back_populates="payment")
