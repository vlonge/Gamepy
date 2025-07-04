from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

class GroupMembership(db.Model):
    charid = db.Column(db.Integer, db.ForeignKey('characters.id'), primary_key=True)
    groupid = db.Column(db.Integer, db.ForeignKey('groups.id'), primary_key=True)
    private = db.Column(db.Boolean)