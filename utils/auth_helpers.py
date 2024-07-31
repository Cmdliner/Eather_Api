import uuid, random
from config.settings import settings
from datetime import datetime, UTC, timedelta
from passlib.context import CryptContext
from pydantic import ValidationError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from schemas.user import TokenPayload

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def create_access_token(subject: str, expires_delta: timedelta | None = None) -> str:
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(
            minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        )

    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(
        to_encode, settings.ACCESS_TOKEN_SECRET, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def create_refresh_token(subject: str, expires_delta: timedelta | None = None) -> str:
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(
            days=int(settings.REFRESH_TOKEN_EXPIRE_DAYS)
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(
        to_encode, settings.REFRESH_TOKEN_SECRET, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def decode_token(token: str, token_secret: str) -> str:
    try:
        payload = jwt.decode(token, token_secret, algorithms=[settings.ALGORITHM])
        email = TokenPayload(**payload).sub
        if email is None:
            raise HTTPException(status_code=403, detail="Invalid Auth Token!")
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid Auth Token")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token, settings.ACCESS_TOKEN_SECRET, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials!",
        )

    return token_data.sub


def generate_OTP():
    return f"{random.randint(0, 9)}-{random.randint(0, 9)}-{random.randint(0, 9)}-{random.randint(0, 9)}-{random.randint(0, 9)}"
