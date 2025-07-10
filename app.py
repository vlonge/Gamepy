import sqlalchemy
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_models.characters import Characters, db
from flask_models.pronouns import Pronouns, load_pronouns
from flask_models.places import Places
from flask_models.groups import Groups, GroupMemberships
from flask_models.goals import Goals, OwnedGoals
from flask_models.items import Items, OwnedItems
from flask_models.stats import Stats, OwnedStats
from flask_models.abilities import Abilities, OwnedAbilities
import secrets
secret_key = secrets.token_hex(16)
# example output, secret_key = 000d88cd9d90036ebdd237eb6b0db000
app = Flask(__name__)

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secret_key
db.init_app(app)
@app.route("/")
def home():
    url = url_for("character")
    return render_template("index.html", url=url)

@app.route("/character")
def character():
    char_list = Characters.query.all()
    proto_prolist = Pronouns.query.all()
    prolist = map(lambda pro: (pro.id, pro.name), proto_prolist)
    prodict = dict(prolist)
    return render_template("character.html", char_list=char_list, prodict=prodict)


@app.route("/character/add", methods=["POST"])
def add_char():
    name = request.form.get("name")
    default_pronoun = Pronouns.query.first().id
    new_char = Characters(name=name, pronouns=default_pronoun)
    db.session.add(new_char)
    db.session.commit()
    return redirect(url_for("character"))


@app.route("/character/update/<int:char_id>", methods=["POST"])
def change_pronouns(char_id):
    char = Characters.query.filter_by(id=char_id).first()
    pro = request.form.get("chosen pronouns")
    pro.strip()
    try:
        pronoun = Pronouns.query.filter_by(name=pro).one()
        char.pronouns=pronoun.id
        #flash("Success!")
    except sqlalchemy.orm.exc.NoResultFound:
        new_pronoun = Pronouns(name=pro)
        db.session.add(new_pronoun)
        char.pronouns=Pronouns.query.filter_by(name=pro).one().id
        #flash("Don't forget to update the Pronouns database with the data for this new pronoun!")
    except sqlalchemy.orm.exc.MultipleResultsFound:
        #flash("Multiple pronouns found. Please clean up Pronouns table and try again later!")
        pass
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
    for pro in pronouns:
        Pronouns.create(pro)
    print("Initialized the database.")

@app.cli.command("drop_db")
def drop_db():
    """Drop the old database."""
    db.drop_all()
    print("Dropped the database.")

if __name__ == "__main__":
    app.run(debug=True)
