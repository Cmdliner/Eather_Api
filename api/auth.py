import uuid
from config.db import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from models.user import User
from schemas.user import UserCreate
from sqlalchemy.orm import Session
from utils.auth_helpers import hash_password

router = APIRouter()


@router.post('/register', status_code=status.HTTP_201_CREATED)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if db_user:
        raise HTTPException(422, detail="Email taken!")
    new_user = User(email=user.email, hashed_password=hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user.email


@router.post('/user_id')
def get_id(user: UserCreate, db: Session = Depends(get_db)):
    user_id = db.query(User).filter(User.email == user.email).first()

    if user_id:
        return user_id.id

    return 'No such user'    