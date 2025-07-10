from sqlalchemy import Column, ForeignKey, Integer, String
from base import Base
from collections import namedtuple
import csv
import os

PronounTuple = namedtuple('PronounTuple',["name", "subject", "object", "attributive_possessive", "nominal_possessive", "reflexive"])

def load_pronouns(csv_name= os.path.abspath('./resources/default_pronouns.csv')):
    """Reads in a csv file of pornouns formatted in order of PronounTuple field names.
    @param: csv_name: name of the csv file to read
    @return: list of PronounTuple objects."""
    pronoun_list = []
    with open(csv_name) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            pronoun_list.append(PronounTuple(*row))
    return pronoun_list

class Pronouns(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subject = Column(String)
    object = Column(String)
    attributive_possessive = Column(String)
    nominal_possessive = Column(String)
    reflexive = Column(String)

 #   @classmethod
 #   def create(cls, pronoun: PronounTuple):
  #      """
   #     creates a Pronouns entry from a PronounTuple object.
    #    @pronoun: PronounTuple object to be entered
     #   """
      #  pro = cls(**pronoun._asdict())
       # print(pro)
        #session.add(pro)
        #session.commit()

