import uuid
from models.base import Base
from sqlalchemy import String, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    email: Mapped[str] = mapped_column(String(50), index=True, unique=True)
    password: Mapped[str] = mapped_column(String(128))

    appointments = relationship("Appointment", back_populates="user")

    def __repr__(self):
        return f"<User(username={self.email})>"
