import uuid
from .base import Base
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Result(Base):
    __tablename__ = "results"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    value: Mapped[str] = mapped_column(String(225), nullable=False)
    test_id: Mapped[str] = mapped_column(ForeignKey("tests.id"))
    
    test = relationship("Test", back_populates="results")
    appointments = relationship(
        "Appointment", secondary="appointment_results", back_populates="results"
    )
    def __repr__(self):
        return f"result<id=({self.id}), value=({self.value})>"