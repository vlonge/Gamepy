from sqlalchemy import Column, ForeignKey, Integer, String
from base import Base

class Characters(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    pronouns = Column(Integer, ForeignKey('pronouns.id'))
    description = Column(String)