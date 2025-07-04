from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Places(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)