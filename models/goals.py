from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Goals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.String)

class OwnedGoals(db.Model):
    goalid = db.Column(db.Integer, db.ForeignKey('goals.id'), primary_key=True)
    charid = db.Column(db.Integer, db.ForeignKey('characters.id'), primary_key=True, nullable=True)
    groupid = db.Column(db.Integer, db.ForeignKey('groups.id'), primary_key=True, nullable=True)
    placeid = db.Column(db.Integer, db.ForeignKey('places.id'), primary_key=True, nullable=True)
