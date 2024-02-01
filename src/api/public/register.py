from pydantic import BaseModel
import fastapi
from fastapi import Depends, HTTPException
from typing import Optional

from sqlalchemy.orm import Session

from src.db.db_setup import get_db
from src.schemas.profile import ProfileCreate
from src.schemas.user import UserCreate
from src.db.utils.user import create_user
from src.db.utils.profile import create_profile

from src.utils.auth import hash_password

router = fastapi.APIRouter()


class RegisterRequestBody(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
    bio: Optional[str]


@router.post("/register")
async def register_user(request: RegisterRequestBody, db: Session = Depends(get_db)):
    db_user = create_user(db, UserCreate(username=request.username, password=hash_password(request.password)))

    new_profile = ProfileCreate(user_id=db_user.id,
                                **request.model_dump(include={"first_name", "last_name", "email", "bio"}))
    new_profile.user_id = db_user.id

    create_profile(db, new_profile)
    return {"message": "sucess!"}
