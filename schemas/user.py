from pydantic import BaseModel, EmailStr


class BaseUser(BaseModel):
    email: EmailStr


class UserCreate(BaseUser):
    password: str


class DbUser(BaseUser):
    id: str
    hashed_password: str


class UserResponse(BaseUser):
    id: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: str | None = None
