from fastapi import APIRouter
from schemas.user import UserIn, UserInDB

router = APIRouter()

@router('/auth/register', status_code=201, response_model=UserInDB)
def register(user: UserIn):
    hashed_password = user.password

    user1 = user.model_dump()
    # user1.update({'password': })