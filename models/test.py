import uuid
from models.base import Base
from sqlalchemy import BINARY, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Test(Base):
    __tablename__ = "tests"

    id: Mapped[bytes] = mapped_column(
        BINARY(16), primary_key=True, default=lambda: uuid.uuid4().bytes
    )
    name: Mapped[str] = mapped_column(String(100), index=True, unique=True)
    price: Mapped[int] = mapped_column(Integer)
    appointments = relationship(
        "Appointment", secondary="appointment_tests", back_populates="tests"
    )

    def __repr__(self):
        return f"Test<name=({self.name}), price=({self.price})>"
