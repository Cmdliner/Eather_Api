from config.db import get_db
from fastapi import APIRouter, Depends, HTTPException, Response, status
from models.user import User
from schemas.user import UserCreate as UserIn
from sqlalchemy.orm import Session
from utils.auth_helpers import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
)

router = APIRouter()

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def signup(user: UserIn, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if db_user:
        raise HTTPException(422, detail="Email taken!")
    new_user = User(email=user.email, hashed_password=hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"success": "User created successfully", "user": new_user.email}


@router.post("/login")
async def sign_in(res: Response, user: UserIn, db: Session = Depends(get_db)):
    user_in_db = db.query(User).filter(User.email == user.email).first()

    if not user_in_db:
        raise HTTPException(403, detail="Invalid username or password")

    passwd_match = verify_password(user.password, user_in_db.hashed_password)

    if not passwd_match:
        raise HTTPException(403, detail="Invalid username or password")

    #! TODO => generate access and refresh tokens and set them in headers and cookies respectively
    access_token = create_access_token(user.email)
    refresh_token = create_refresh_token(user.email)
    res.headers.append("Authorization", f"Bearer {access_token}")
    res.set_cookie(
        key="refresh",
        value=f"Bearer {refresh_token}",
        max_age=7 * 24 * 60 * 60,
        httponly=True,
        samesite="lax",
    )
    return {"success": "User logged in succesfully"}
