from pydantic import BaseModel, EmailStr


class BaseUser(BaseModel):
    email: EmailStr


class UserCreate(BaseUser):
    password: str


class DbUser(BaseUser):
    id: str
    password: str


class UserResponse(BaseUser):
    id: str

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: str | None = None
