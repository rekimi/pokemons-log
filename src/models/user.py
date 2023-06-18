from sqlalchemy import Boolean, Column, Integer, String, DateTime 
from src.db import Base
from datetime import datetime

# please import this class to db.__init__.py

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), nullable=False, index=True)
    password = Column(String(255), nullable=False, index=True)

    created_at = Column(DateTime(), default=datetime.now())
    deleted = Column(Boolean(), default=False)
