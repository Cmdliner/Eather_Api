from sqlalchemy import Table, Column, String, ForeignKey
from .base import Base

appointment_tests = Table(
    "appointment_tests",
    Base.metadata,
    Column("appointment_id", String(32), ForeignKey("appointments.id")),
    Column("test_id", String(32), ForeignKey('tests.id'))
)
