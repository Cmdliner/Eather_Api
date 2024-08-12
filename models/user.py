import uuid
from .base import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List
from .appointment import Appointment


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    email: Mapped[str] = mapped_column(
        String(100), index=True, unique=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)

    appointments: Mapped[List["Appointment"]] = relationship(
        "Appointment", back_populates="user", cascade="all, delete-orphan"
    )
    
