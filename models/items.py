from models.characters import db

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    effects = db.Column(db.String)

class OwnedItems(db.Model):
    itemid = db.Column(db.Integer, db.ForeignKey('items.id'), primary_key=True)
    charid = db.Column(db.Integer, db.ForeignKey('characters.id'), primary_key=True, nullable=True)
    groupid = db.Column(db.Integer, db.ForeignKey('groups.id'), primary_key=True, nullable=True)
    placeid = db.Column(db.Integer, db.ForeignKey('places.id'), primary_key=True, nullable=True)