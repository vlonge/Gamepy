from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import characters
import stats
app = Flask(__name__)

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Goals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.Text)

class CharacterGoals(db.Model):
    # charid integer [ref: <> characters.id]
    # goalid integer [ref: > goals.id]
    pass

class GroupGoals(db.Model):
    # groupid integer [ref: <> groups.id]
    # goalid integer [ref: > goals.id]
    pass