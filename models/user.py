import uuid
from config.db import Base
from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.mysql import BINARY
from sqlalchemy.ext.hybrid import  hybrid_property


class User(Base):
    __tablename__ = "users"

    id = Column(BINARY(16), primary_key=True, default=lambda: uuid.uuid4().bytes)    
    email = Column(String(50), unique=True, index=True, nullable=False)
    username = Column(String(20), unique=True, index=True)
    hashed_password = Column(String(255), nullable=False)
    is_superuser = Column(Boolean)

    

    def generate_username(self):
        if not self.username:
            username = self.email.split("@")[0] + str(uuid.uuid4()[:8])
            self.username = username

    @hybrid_property
    def uuid(self):
        return uuid.UUID(bytes=self.id)

    @uuid.setter
    def uuid(self, uuid_value):
        self.id = uuid_value.bytes
