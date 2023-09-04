from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    interests = db.Column(db.String(255), nullable=False)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")

@app.route("/registration", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        gender = request.form.get("gender")
        interests = request.form.get("interests")

        new_user = User(name=name, gender=gender, interests=interests)
        db.session.add(new_user)
        db.session.commit()

        return render_template("confirmation.html")

    return render_template("registration.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
