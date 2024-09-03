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
        "Appointment", secondary="appointment_tests", back_populates="results"
    )

    # TODO => describe relationship between test values in appointments as results for them here
