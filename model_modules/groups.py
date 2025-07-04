from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

class GroupMembership(db.Model):
    """TODO:
    charid integer [ref: <> characters.id]
    groupid integer [ref: <> groups.id]
    private boolean
    """
    pass