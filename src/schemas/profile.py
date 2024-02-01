from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ProfileBase(BaseModel):
    email: str
    first_name: str
    last_name: str
    bio: Optional[str] = None
    user_id: int


class ProfileCreate(ProfileBase):
    pass


class Profile(ProfileBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
