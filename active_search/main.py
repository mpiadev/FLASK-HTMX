from pathlib import Path

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

BASE_DIR = Path(__file__).resolve().parent

app = Flask(
    __name__,
    instance_path=BASE_DIR,
    template_folder=BASE_DIR / "assets/templates",
    static_folder=BASE_DIR / "assets/static"
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
        return f"{self.first_name}-{self.last_name}"


@app.route("/")
def index():
    persons = Person.query.all()
    return render_template("index.html", persons=persons)


@app.route("/search")
def search():
    q = request.args.get("q")

    if q:
        persons = Person.query.filter(
            Person.first_name.contains(q)|
            Person.last_name.contains(q)
        )
    else: 
        persons = Person.query.all()
    return render_template("partials/persons.html", persons=persons)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)