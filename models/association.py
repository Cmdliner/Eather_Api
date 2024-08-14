from models.base import Base
from sqlalchemy import Table, Column, BINARY, ForeignKey

appointment_tests = Table(
    "appointment_tests",
    Base.metadata,
    Column(
        "appointment_id", BINARY(16), ForeignKey("appointments.id"), primary_key=True
    ),
    Column("test_id", BINARY(16), ForeignKey("tests.id"), primary_key=True),
)
