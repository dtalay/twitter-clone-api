from sqlalchemy import Text, Column, Integer, String, DateTime, ForeignKey

from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from sqlalchemy_utils import EmailType

from ..db_setup import Base
from .mixins import Timestamp


class Profile(Timestamp, Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(EmailType, unique=True, index=True, nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    bio = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="profile")
