from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Goals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.String)

class OwnedGoals(db.Model):
    """
    Table owned_goals{
    goalid integer [ref: <> goals.id]
    charid intger [ref: <> characters.id, null]
    groupid integer [ref: <> groups.id, null]
    placeid integer [ref: <> places.id, null]
    }
    """
    pass