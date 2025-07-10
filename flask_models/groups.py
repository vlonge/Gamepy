from models.characters import db


class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

class GroupMemberships(db.Model):
    charid = db.Column(db.Integer, db.ForeignKey('characters.id'), primary_key=True)
    groupid = db.Column(db.Integer, db.ForeignKey('groups.id'), primary_key=True)
    private = db.Column(db.Boolean)