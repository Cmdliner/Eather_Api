import re
from pydantic import BaseModel, EmailStr, Field

username_pattern = re.compile(r"[a-z]")
# password_patterm =


class BaseUser(BaseModel):
    # username: str = Field(min_length=3, pattern=username_pattern)
    email: EmailStr
    is_superuser: bool = Field(default=False)


class UserCreate(BaseUser):
    password: str = Field(min_length=6)


class UserUpdate(BaseUser):
    password: str = Field(min_length=6)


class UserInDbBase(BaseUser):
    id: str | None = None

    class Config:
        from_attributes = True


class UserInDB(UserInDbBase):
    hashed_password: str


class User(UserInDB):
    pass


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: str | None = None
