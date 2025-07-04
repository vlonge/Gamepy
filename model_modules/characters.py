from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    pronouns = db.Column(db.Integer) #TODO: [ref: > pronouns.id]
    description = db.Column(db.String)