import re
from pydantic import BaseModel, EmailStr, Field

username_pattern = re.compile(r"[a-z]")
# password_patterm =


class BaseUser(BaseModel):
    username: str = Field(min_length=3, pattern=username_pattern)
    email: EmailStr
    is_superuser: bool = Field(default=False)

class UserIn(BaseUser):
    password: str = Field(min_length=6)


class UserInDB(BaseUser):
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: str | None = None
