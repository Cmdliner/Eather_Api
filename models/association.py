from models.base import Base
from sqlalchemy import Table, Column, String, ForeignKey

appointment_tests = Table(
    "appointment_tests",
    Base.metadata,
    Column(
        "appointment_id", String(36), ForeignKey("appointments.id"), primary_key=True
    ),
    Column("test_id", String(36), ForeignKey("tests.id"), primary_key=True),
)

appointment_results = Table(
    "appointment_results",
    Base.metadata,
    Column("appointment_id", String(36), ForeignKey("appointments.id"), primary_key=True),
    Column("result_id", String(36), ForeignKey("results.id"), primary_key=True),
)