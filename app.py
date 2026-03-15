from flask import Flask, render_template, request, redirect, session
from model import predict_movie
from config import get_db
from flask import session, redirect, url_for
import pandas as pd
from model import predict_movie

movies = pd.read_csv("movies.csv")

def recommend_movies(genre):

    filtered = movies[movies["genre"] == genre]

    suggestions = filtered["title"].head(5).tolist()


    return suggestions

app = Flask(__name__)
app.secret_key = "secret123"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        db = get_db()
        cursor = db.cursor()

        cursor.execute(
        "INSERT INTO users(name,email,password) VALUES(%s,%s,%s)",
        (name,email,password))

        db.commit()

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        db = get_db()
        cursor = db.cursor()

        cursor.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (email,password))

        user = cursor.fetchone()

        if user:
            session["user"] = user[0]
            return redirect("/dashboard")

    return render_template("login.html")

def recommend_movies(genre):

    results = movies[movies["genre"] == genre]

    return results["title"].head(5).tolist()

@app.route("/predict", methods=["GET","POST"])
def predict():

    if request.method == "POST":

        genre = request.form.get("genre")
        budget = request.form.get("budget")
        runtime = request.form.get("runtime")

        rating, success = predict_movie(genre, budget, runtime)

        return render_template(
            "predict.html",
            rating=rating,
            success=success
        )

    return render_template("predict.html")

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM predictions WHERE user_id=%s",
        (session["user"],)
    )

    history = cursor.fetchall()

    return render_template("dashboard.html", history=history)


if __name__ == "__main__":
    app.run(debug=True)