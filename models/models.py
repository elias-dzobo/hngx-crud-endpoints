from db.database import Base 
from sqlalchemy import TIMESTAMP, Column, String, Boolean 
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE



class User(Base):
    __tablename__ = 'users'
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    name = Column(String, nullable=False) 
    track = Column(String, nullable=False)
    