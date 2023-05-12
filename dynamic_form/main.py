from pathlib import Path

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired

BASE_DIR = Path(__file__).resolve().parent

app = Flask(
    __name__,
    template_folder=BASE_DIR / "assets/templates",
    static_folder=BASE_DIR / "assets/static",
    instance_path=BASE_DIR
)
app.config["SECRET_KEY"] = "top-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

db = SQLAlchemy(app)
bootstrap = Bootstrap5(app)


class Person(db.Model):
    __tablename__ = "persons"
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ContactForm(FlaskForm):
    first_name = StringField(
        label="Prénom",
        validators=[DataRequired()]
    )
    last_name = StringField(
        label="Nom",
        validators=[DataRequired()]
    )
    submit = SubmitField(label="Ajouter")


@app.route("/")
def index():
    personnes = Person.query.order_by(Person.id.asc())
    form = ContactForm()
    return render_template("index.html", form=form, personnes=personnes)


@app.route("/add_person/", methods=["GET", "POST"])
def add_person():
    form = ContactForm()

    if request.method == "POST":
        first_name = form.first_name.data
        last_name = form.last_name.data

        new_person = Person(
            first_name=first_name,
            last_name=last_name
        )
        db.session.add(new_person)
        db.session.commit()

        return render_template("partials/persons.html", personne=new_person)

    elif form.errors:
        pass
    return render_template("partials/form.html", form=form)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

