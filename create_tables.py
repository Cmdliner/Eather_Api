from config.db import engine
from models.appointment import Base as AppointmentBase
from models.user import Base as UserBase
from models.test import Base as TestBase
from models.association import appointment_tests  # Import the association table


def create_tables():
    # Create a new MetaData object
    from sqlalchemy import MetaData

    combined_metadata = MetaData()

    # Combine the metadata from all your models
    for base in (UserBase, TestBase, AppointmentBase):
        for table in base.metadata.tables.values():
            table.tometadata(combined_metadata)

    # Add the association table to the combined metadata
    appointment_tests.tometadata(combined_metadata)

    # Create all tables
    combined_metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    print("Database tables created successfully")
