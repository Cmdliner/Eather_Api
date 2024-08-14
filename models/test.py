import uuid
from models.base import Base
from sqlalchemy import BINARY, Integer, String, TEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Test(Base):
    __tablename__ = "tests"

    id: Mapped[bytes] = mapped_column(
        BINARY(16), primary_key=True, default=lambda: uuid.uuid4().bytes
    )
    name: Mapped[str] = mapped_column(String(100), index=True, unique=True)
    description: Mapped[str] = mapped_column(TEXT, nullable=True)
    price: Mapped[int] = mapped_column(Integer)
    appointments = relationship(
        "Appointment", secondary="appointment_tests", back_populates="tests"
    )

    def __repr__(self):
        return f"Test<name=({self.name}), price=({self.price})>"
