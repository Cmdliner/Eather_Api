import uuid
from models.base import Base
from sqlalchemy import BINARY, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from .appointment import Appointment


class User(Base):
    __tablename__ = "users"

    id: Mapped[bytes] = mapped_column(
        BINARY(16), primary_key=True, default=lambda: uuid.uuid4().bytes
    )
    email: Mapped[str] = mapped_column(String(50), index=True, unique=True)
    password: Mapped[str] = mapped_column(String(128))

    appointments = relationship("Appointment", back_populates="user")

    def __repr__(self):
        return f"<User(username={self.email})>"
