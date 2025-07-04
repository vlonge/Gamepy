from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)

class OwnedStats(db.Model):
    statid = db.Column(db.Integer, db.ForeignKey('stats.id'), primary_key=True)
    charid = db.Column(db.Integer, db.ForeignKey('characters.id'), primary_key=True, nullable=True)
    groupid = db.Column(db.Integer, db.ForeignKey('groups.id'), primary_key=True, nullable=True)
    placeid = db.Column(db.Integer, db.ForeignKey('places.id'), primary_key=True, nullable=True)
    itemid = db.Column(db.Integer, db.ForeignKey('items.id'), primary_key=True, nullable=True)
    stat_value = db.Column(db.String)
