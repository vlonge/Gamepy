from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models.characters import Characters
from models.pronouns import Pronouns, load_pronouns
from models.places import Places
from models.groups import Groups, GroupMemberships
from models.goals import Goals, OwnedGoals
from models.items import Items, OwnedItems
from models.stats import Stats, OwnedStats
from models.abilities import Abilities, OwnedAbilities

app = Flask(__name__)

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def home():
    url = url_for("character")
    return render_template("index.html", url=url)

@app.route("/character")
def character():
    char_list = Characters.query.all()
    gender_list=Pronouns.query.all()
    gender_list = map(lambda gender: gender.name, gender_list)
    return render_template("character.html", char_list=char_list, gender_list=gender_list)


@app.route("/character/add", methods=["POST"])
def add_char():
    name = request.form.get("name")
    default_pronoun = Pronouns.query.first().name
    new_char = Characters(name=name, gender=default_pronoun)
    db.session.add(new_char)
    db.session.commit()
    return redirect(url_for("character"))


@app.route("/character/update/<int:char_id>", methods=["POST"])
def change_gender(char_id):
    char = Characters.query.filter_by(id=char_id).first()
    char.gender = request.form.get("chosen gender")
    if not char.gender in map(lambda x: x.name, Pronouns.query.all()):
        flash("Don't forget to update the Prounouns database with this new gender!")
    db.session.commit()
    return redirect(url_for("character"))


@app.route("/character/delete/<int:char_id>")
def delete_char(char_id):
    char = Characters.query.filter_by(id=char_id).first()
    db.session.delete(char)
    db.session.commit()
    return redirect(url_for("character"))


@app.cli.command("init_db")
def init_db():
    """ Initialize the database."""
    db.create_all()
    pronouns = load_pronouns()
    Pronouns.create(*pronouns)
    print("Initialized the database.")

if __name__ == "__main__":
    app.run(debug=True)
