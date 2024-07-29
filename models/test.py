""" from config.db import Base
from sqlalchemy import Column, String, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Test(Base):
    __tablename__ = "tests"

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String, unique=True, index=True, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(255))

    appointments = relationship(
        "Appointment", secondary="appointment_tests", back_populates="recommended_tests"
    )
 """