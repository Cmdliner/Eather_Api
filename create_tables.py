from config.db import engine
# from models.user import Base as UserBase
from models.test import Base as TestBase


def create_tables():
    # UserBase.metadata.create_all(bind=engine)
    TestBase.metadata.create_all(bind=engine)



if __name__ == "__main__":
    create_tables()
    print("Database tables created successfully")
