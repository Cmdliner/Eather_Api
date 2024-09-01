import uuid
from models.base import Base
from sqlalchemy import String, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    first_name: Mapped[str] = mapped_column(String(50), nullable=True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=True)
    gender: Mapped[str] = mapped_column(String(1), nullable=True)
    nationality: Mapped[str] = mapped_column(String(50), nullable=True)
    email: Mapped[str] = mapped_column(String(50), index=True, unique=True)
    password: Mapped[str] = mapped_column(String(128))

    appointments = relationship("Appointment", back_populates="user")

    def __repr__(self):
        return f"<User(username={self.email})>"
