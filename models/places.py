from sqlalchemy import Column, ForeignKey, Integer, String
from base import Base

class Places(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)