from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    interests = db.Column(db.String(255))  # Assuming you want to store interests as a string

    def __init__(self, first_name, last_name, phone_number, email, gender, interests):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.gender = gender
        self.interests = interests
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")

@app.route("/registration", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        phone_number = request.form.get("phone_number")
        email = request.form.get("email")
        gender = request.form.get("gender")

        interests =[]

        if 'music' in request.form:
            interests.append('music')

        if 'travel' in request.form:
            interests.append('travel')

        if 'cooking' in request.form:
            interests.append('cooking')

        if 'sports' in request.form:
            interests.append('sports')

        if 'art' in request.form:
            interests.append('art')

        if 'reading' in request.form:
            interests.append('reading')

        if 'hiking' in request.form:
            interests.append('hiking')

        if 'photography' in request.form:
            interests.append('photography')

        if 'gaming' in request.form:
            interests.append('gaming')

        if 'fashion' in request.form:
            interests.append('fashion')

        if 'movies' in request.form:
            interests.append('movies')

        if 'technology' in request.form:
            interests.append('technology')

        if 'cooking' in request.form:
            interests.append('cooking')

        if 'yoga' in request.form:
            interests.append('yoga')

        if 'dancing' in request.form:
            interests.append('dancing')

        if 'fitness' in request.form:
            interests.append('fitness')

        if 'camping' in request.form:
            interests.append('camping')

        if 'writing' in request.form:
            interests.append('writing')

        if 'crafts' in request.form:
            interests.append('crafts')

        if 'foodie' in request.form:
            interests.append('foodie')

        if 'history' in request.form:
            interests.append('history')

        if 'science' in request.form:
            interests.append('science')

        if 'nature' in request.form:
            interests.append('nature')

        if 'diy' in request.form:
            interests.append('diy')

        if 'pets' in request.form:
            interests.append('pets')

        if 'volunteering' in request.form:
            interests.append('volunteering')

        if 'meditation' in request.form:
            interests.append('meditation')

        if 'outdoor_activities' in request.form:
            interests.append('outdoor activities')

        interests_str = ','.join(interests)

        new_user = User(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            gender=gender,
            interests=interests_str,
        )

        db.session.add(new_user)
        db.session.commit()

        return render_template("confirmation.html")

    return render_template("registration.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
