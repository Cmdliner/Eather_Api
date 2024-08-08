""" from config.db import engine
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
    combined_metadata.add_all([appointment_tests])

    # Create all tables
    combined_metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
    print("Database tables created successfully") """

from config.db import engine
from models.appointment import Appointment as AppointmentBase
from models.user import User as UserBase
from models.test import Test as TestBase
from models.association import appointment_tests

# Import the MetaData class from sqlalchemy
from sqlalchemy import MetaData

def create_tables():
    # Create a new MetaData object
    combined_metadata = MetaData()

    # Add the tables from your models to the combined metadata
    for base in (UserBase, TestBase, AppointmentBase):
        for table in base.metadata.tables.values():
            table.metadata = combined_metadata

    # Add the association table to the combined metadata
    combined_metadata.add_all([appointment_tests])

    # Create all tables
    combined_metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
    print("Database tables created successfully")