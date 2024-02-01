import fastapi
from datetime import datetime, timedelta, timezone
from os import environ
from typing import Annotated
from fastapi import Depends, HTTPException, status

from src.schemas.user import TokenData, User

from src.utils.auth import get_current_active_user

router = fastapi.APIRouter()


@router.get("/users/me/", response_model=User)
async def read_users_me(
        current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user
