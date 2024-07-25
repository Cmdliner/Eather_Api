import uuid
from config.db import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)

    def generate_username(self):
        if not self.username:
            username = self.email.split("@")[0] + str(uuid.uuid4()[:8])
            self.username = username
