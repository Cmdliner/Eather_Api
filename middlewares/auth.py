from config.db import get_db
from config.settings import settings
from fastapi import Depends, HTTPException, Request
from models.user import User
from sqlalchemy.orm import Session
from utils.auth_helpers import decode_token


async def require_auth(req: Request, db: Session = Depends(get_db)):
    auth_header = None
    for header in req.headers.keys():
        if header.lower() == "authorization":
                auth_header = header

    if not bool(auth_header):
        raise HTTPException(status_code=401, detail="Unauthorized!")

    access_token = req.headers.get("Authorization").split(" ")[-1]
    payload = decode_token(access_token, settings.ACCESS_TOKEN_SECRET)

    db_user = db.query(User).filter(User.email == payload.get("sub")).first()
    if db_user is None:
        raise HTTPException(status_code=403, detail="User not found!")

    return
