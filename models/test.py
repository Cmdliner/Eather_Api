import uuid
from models.base import Base
from sqlalchemy import Integer, String, TEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Test(Base):
    __tablename__ = "tests"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    name: Mapped[str] = mapped_column(String(100), index=True, unique=True)
    description: Mapped[str] = mapped_column(TEXT, nullable=True)
    price: Mapped[int] = mapped_column(Integer)
    appointments = relationship(
        "Appointment", secondary="appointment_tests", back_populates="tests"
    )
    results = relationship("Result", back_populates="test")

    def __repr__(self):
        return f"Test<name=({self.name}), price=({self.price})>"
