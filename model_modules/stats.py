from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)

class OwnedStats(db.Model):
    """TODO:
    Table owned_stats{
      statid integer [ref: <> stats.id]
      stat_value String
      charid intger [ref: > characters.id, null]
      groupid integer [ref: > groups.id, null]
      placeid integer [ref: > places.id, null]
      itemid integer [ref: > items.id, null]
    }
    """
    pass
