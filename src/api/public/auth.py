from datetime import datetime, timedelta, timezone
from pydantic import BaseModel
import fastapi
from fastapi import Depends, HTTPException, status
from typing import Annotated

from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from src.db.db_setup import get_db
from src.schemas.profile import ProfileCreate
from src.schemas.user import UserCreate
from src.db.utils.user import create_user
from src.db.utils.profile import create_profile

from src.utils.auth import hash_password
from src.utils.auth import authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from src.schemas.user import Token

router = fastapi.APIRouter()


@router.post("/token")
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)
) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
