import uuid
from config.db import get_db
from config.settings import settings
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from schemas.user import Token, User, UserCreate
from sqlalchemy.orm import Session
from utils.auth_helpers import verify_password, create_access_token, hash_password

router = APIRouter()


@router("/register", response_model=User, status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=400, detail="User with that email alredy exists!"
        )
    new_user = User(
        email=user.email,
        hashed_password=hash_password(user.password),
        is_superuser=False,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)


@router("/login", response_model=Token)
async def login(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    user = db.query(User).filter(User.email == form_data.email).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWWAuthenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCES)
    return {
        "access_token": create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "Bearer",
    }
