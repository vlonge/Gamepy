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
    gender = db.Column(db.Integer)


@app.route("/character")
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@app.route("/character/add", methods=["POST"])
def add_char():
    name = request.form.get("name")
    new_char = Character(name, (int) Gender.THEY)
    db.session.add(Character)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/character/update/<int:todo_id>")
def change_gender(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/character/delete/<int:todo_id>")
def delete_char(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.cli.command("init_db")
def init_db():
    """ Initialize the database."""
    db.create_all()
    print("Initialized the database.")

if __name__ == "__main__":
    app.run(debug=True)
