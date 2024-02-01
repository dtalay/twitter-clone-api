from sqlalchemy.orm import Session
from src.schemas.profile import ProfileCreate
from src.db.models.profile import Profile


def create_profile(db: Session, profile: ProfileCreate):
    db_profile = Profile(email=profile.email, first_name=profile.first_name, last_name=profile.last_name,
                         bio=profile.bio, user_id=profile.user_id)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile
