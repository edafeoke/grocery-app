from sqlalchemy import Boolean, Column, Integer, String, Float
# from sqlalchemy.orm import relationship
from ..database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    balance = Column(Float)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
