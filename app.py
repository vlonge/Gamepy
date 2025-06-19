from attr.validators import instance_of
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from collections import namedtuple
import csv
from enum import Enum
app = Flask(__name__)

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

PronounTuple = namedtuple('PronounTuple',["name", "subject", "object", "attributive_possessive", "nominal_possessive", "reflexive"])

def load_pronouns(csv_name='default_pronouns.csv'):
    """Reads in a csv file of pornouns formatted in order of PronounTuple field names.
    @param: csv_name: name of the csv file to read
    @return: list of PronounTuple objects."""
    pronoun_list = []
    with open(csv_name) as csvfile:
        reader = csv.reader(csvfile)
        pronoun_list.append(PronounTuple(*next(reader)))
    return pronoun_list


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    #TODO description
    #TODO groups
    #TODO abilities
    #TODO stats

class Pronouns(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    subject = db.Column(db.String(100))
    object = db.Column(db.String(100))
    attributive_possessive = db.Column(db.String(100))
    nominal_possessive = db.Column(db.String(100))
    reflexive = db.Column(db.String(100))


#TODO: tex integration? way to find and replace genders to put the appropriate one with the appropriate form where applicable?

#TODO Groups table
#TODO Abilities table
#TODO stats table
@app.route("/")
def home():
    url = url_for("character")
    return render_template("index.html", url=url)

@app.route("/character")
def character():
    char_list = Character.query.all()
    gender_list=Pronouns.query.all()
    gender_list = map(lambda gender: gender.name, gender_list)
    return render_template("character.html", char_list=char_list, gender_list=gender_list)


@app.route("/character/add", methods=["POST"])
def add_char():
    name = request.form.get("name")
    default_pronoun = Pronouns.query.first().name
    new_char = Character(name=name, gender=default_pronoun)
    db.session.add(new_char)
    db.session.commit()
    return redirect(url_for("character"))


@app.route("/character/update/<int:char_id>", methods=["POST"])
def change_gender(char_id):
    char = Character.query.filter_by(id=char_id).first()
    char.gender = request.form.get("chosen gender")
    if not char.gender in map(lambda x: x.name, Pronouns.query.all()):
        flash("Don't forget to update the Prounouns database with this new gender!")
    db.session.commit()
    return redirect(url_for("character"))


@app.route("/character/delete/<int:char_id>")
def delete_char(char_id):
    char = Character.query.filter_by(id=char_id).first()
    db.session.delete(char)
    db.session.commit()
    return redirect(url_for("character"))


@app.cli.command("init_db")
def init_db():
    """ Initialize the database."""
    db.create_all()

    # populate Pronouns table with default pronouns
    for pronoun in load_pronouns():
        pro_row = Pronouns(name=pronoun.name, subject=pronoun.subject, object=pronoun.object,
                           attributive_possessive=pronoun.attributive_possessive,
                           nominal_possessive=pronoun.nominal_possessive, reflexive=pronoun.reflexive)
        db.session.add(pro_row)
    db.session.commit()

    print("Initialized the database.")

if __name__ == "__main__":
    app.run(debug=True)
