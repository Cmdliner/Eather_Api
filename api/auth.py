from datetime import datetime, UTC
from config.db import get_db
from config.settings import settings
from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from models.user import User
from schemas.user import UserCreate as UserIn
from sqlalchemy.orm import Session
from utils.auth_helpers import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    decode_token,
)

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def signup(user: UserIn, db: Session = Depends(get_db)):
    try:
        db_user = db.query(User).filter(User.email == user.email).first()

        if db_user:
            raise HTTPException(422, detail="Email taken!")
        new_user = User(email=user.email, hashed_password=hash_password(user.password))
        print(new_user)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"success": "User created successfully", "user": new_user.email}
    except Exception as err:
        print(f'{err}')
        raise HTTPException(status_code=500, detail="Error creating user")


@router.post("/login")
async def sign_in(res: Response, user: UserIn, db: Session = Depends(get_db)):
    try:
        user_in_db = db.query(User).filter(User.email == user.email).first()

        if not user_in_db:
            raise HTTPException(403, detail="Invalid username or password")

        passwd_match = verify_password(user.password, user_in_db.hashed_password)

        if not passwd_match:
            raise HTTPException(403, detail="Invalid username or password")

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
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error login in user",
        )


@router.post("/refresh")
async def refresh_access_token(
    req: Request, res: Response, db: Session = Depends(get_db)
):
    try:
        refresh_token = req.cookies.get("refresh").split(" ")[-1]
        decoded = decode_token(refresh_token, settings.REFRESH_TOKEN_SECRET)

        if datetime.utcfromtimestamp(decoded.get("exp")) < datetime.now():
            raise HTTPException(403, detail="Auth Session Expired!")

        db_user = db.query(User).filter(User.email == decoded.get("sub")).first()

        if not db_user:
            raise HTTPException(status_code=403, detail="User not found!")

        access_token = create_access_token(decoded.get("sub"))
        res.headers.append("Authorization", f"Bearer {access_token  }")

        return {"success": "Access token refreshed"}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )
