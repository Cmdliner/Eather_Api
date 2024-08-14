from models.base import Base
from config.db import engine


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    print("Creating tables...")
    init_db()
    print("DONE :)")
