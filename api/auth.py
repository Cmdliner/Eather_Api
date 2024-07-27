from config.db import get_db
from config.settings import settings
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from schemas.user import Token, User
from sqlalchemy.orm import Session
from utils.auth_helpers import verify_password, create_access_token

router = APIRouter()


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
