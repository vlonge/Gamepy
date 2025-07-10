from sqlalchemy import Column, ForeignKey, Integer, String
from base import Base

class Goals(Base):
    id = Column(Integer, primary_key=True)
    goal = Column(String)

class OwnedGoals(Base):
    goalid = Column(Integer, ForeignKey('goals.id'), primary_key=True)
    charid = Column(Integer, ForeignKey('characters.id'), primary_key=True, nullable=True)
    groupid = Column(Integer, ForeignKey('groups.id'), primary_key=True, nullable=True)
    placeid = Column(Integer, ForeignKey('places.id'), primary_key=True, nullable=True)
