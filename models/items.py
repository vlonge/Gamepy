from sqlalchemy import Column, ForeignKey, Integer, String
from base import Base

class Items(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    effects = Column(String)

class OwnedItems(Base):
    itemid = Column(Integer, ForeignKey('items.id'), primary_key=True)
    charid = Column(Integer, ForeignKey('characters.id'), primary_key=True, nullable=True)
    groupid = Column(Integer, ForeignKey('groups.id'), primary_key=True, nullable=True)
    placeid = Column(Integer, ForeignKey('places.id'), primary_key=True, nullable=True)