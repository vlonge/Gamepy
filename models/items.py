from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    effects = db.Column(db.String)

class OwnedItems(db.Model):
    """ TODO:
    Table owned_items{
      itemid integer [ref: <> items.id]
      charid intger [ref: <> characters.id, null]
      groupid integer [ref: <> groups.id, null]
      placeid integer [ref: <> places.id, null]

    }
    """
    pass