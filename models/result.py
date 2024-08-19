import uuid
from .base import Base
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column


class Result(Base):
    __tablename__ = "results"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    appointment: Mapped[str] = mapped_column(ForeignKey("appointments.id"), unique=True)

    # TODO => describe relationship between test values in appointments as results for them here
