import uuid
from .base import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from utils.user_roles import UserRoles


class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    role = Column(String(20), default=UserRoles.user)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)

    appointments = relationship("Appointment", back_populates="user")
