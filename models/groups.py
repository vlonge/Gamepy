from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from base import Base


class Groups(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

class GroupMemberships(Base):
    charid = Column(Integer, ForeignKey('characters.id'), primary_key=True)
    groupid = Column(Integer, ForeignKey('groups.id'), primary_key=True)
    private = Column(Boolean)