from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from enum import Enum 

app = Flask(__name__)

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Gender(Enum): 
    OTHER = 0
    THEY = 1
    SHE = 2
    HE = 3

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    gender = db.Column(db.Enum(Gender))
    
@app.route("/")
def home():
    url = url_for("character")
    return render_template("index.html", url=url)

@app.route("/character")
def character():
    char_list = Character.query.all()
    return render_template("character.html", char_list=char_list)


@app.route("/character/add", methods=["POST"])
def add_char():
    name = request.form.get("name")
    new_char = Character(name=name, gender=Gender.THEY)
    db.session.add(new_char)
    db.session.commit()
    return redirect(url_for("character"))


@app.route("/character/update/<int:char_id>")
def change_gender(char_id):
    char = Character.query.filter_by(id=char_id).first()
    gendint = char.gender.value
    gendint += 1
    gendint %= len(Gender)
    char.gender = Gender(gendint)
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
    print("Initialized the database.")

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
