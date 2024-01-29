from sqlalchemy import Boolean, Column,  Integer, String, DateTime


from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null



from ..db_setup import Base
from .mixins import Timestamp


class User(Timestamp, Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), unique=True, index=True, nullable=False)
    password = Column(String(60), nullable=False)

    profile = relationship("Profile", back_populates="user", uselist=False)