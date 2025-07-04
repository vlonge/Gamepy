from collections import namedtuple
import csv
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
PronounTuple = namedtuple('PronounTuple',["name", "subject", "object", "attributive_possessive", "nominal_possessive", "reflexive"])

def load_pronouns(csv_name='default_pronouns.csv'):
    """Reads in a csv file of pornouns formatted in order of PronounTuple field names.
    @param: csv_name: name of the csv file to read
    @return: list of PronounTuple objects."""
    pronoun_list = []
    with open(csv_name) as csvfile:
        reader = csv.reader(csvfile)
        pronoun_list.append(PronounTuple(*next(reader)))
    return pronoun_list

class Pronouns(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    subject = db.Column(db.String)
    object = db.Column(db.String)
    attributive_possessive = db.Column(db.String)
    nominal_possessive = db.Column(db.String)
    reflexive = db.Column(db.String)

    @classmethod
    def create(cls, pronoun: PronounTuple):
        """
        creates a Pronouns entry from a PronounTuple object.
        @pronoun: PronounTuple object to be entered
        """
        pro = cls(**pronoun._asdict())
        db.sesion.add(pro)
        db.commit()

