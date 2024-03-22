from flask import Flask, redirect, render_template, session, request
from flask_session import Session
from functools import wraps  # for login_required
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
import re

app = Flask(__name__)

db = SQL("sqlite:///grades.db")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
selected_subject = None


def login_required(f):  # this is copied from cs50/flask 9/pset/finance/helpers.py
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    # also the link above isn't available for me it just says not found :(

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


@app.route("/")
@login_required
def index():
    grade_dict = db.execute(
        "SELECT * FROM grades WHERE user_id = ?", session["user_id"]
    )
    user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])[0]
    for subject in grade_dict:
        try:
            subject["oral"] = "%.2f" % float(subject["oral"])
            subject["written"] = "%.2f" % float(subject["written"])
            subject["grade"] = "%.3f" % float(subject["grade"])
        except ValueError:
            None
    return render_template("index.html", grade_dict=grade_dict, name=user["real_name"])


@app.route("/login", methods=["POST", "GET"])
def login():
    session.clear()

    if request.method == "GET":
        return render_template("login.html")

    elif request.method == "POST":
        password = request.form.get("password")
        if not password:
            return fault("Must provide password!")

        user_name = request.form.get("user_name")
        if not user_name:
            return fault("Must provide username!")

        user = db.execute("SELECT * FROM users WHERE user_name = ?", user_name)

        try:
            user = user[0]
        except IndexError:
            return fault("Wrong Password or Username!")

        if check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["user_name"] = user["user_name"]
            session["real_name"] = user["real_name"]
            return redirect("/")
        else:
            return fault("Wrong Password or Username!")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/register", methods=["POST", "GET"])
def register():
    session.clear()

    if request.method == "GET":
        return render_template("register.html")

    elif request.method == "POST":
        user_name = request.form.get("user_name")
        if not user_name:
            return fault("Must provide username!")
        taken_username = db.execute(
            "SELECT id FROM users WHERE user_name = ?", user_name
        )
        if taken_username:
            return fault("Username is already registered!")

        real_name = request.form.get("real_name")

        if not real_name:
            return fault("Must provide real name!")

        if _ := not re.search("^[a-zA-Z]+,*[a-zA-Z]+", real_name):
            return fault(
                "Real Name doesn't match format! Mak sure you enter {Firtstname, Lastname}!"
            )

        password = request.form.get("password")
        if not password:
            return fault("Must provide password!")

        confirmation = request.form.get("confirmation")
        if not confirmation:
            return fault("Must confirm Password!")

        if password != confirmation:
            return fault("Password and Confirmation don't match!")
        else:
            password = generate_password_hash(password, method="pbkdf2")

        db.execute(
            "INSERT INTO users (real_name, user_name, password) VALUES (?, ?, ?)",
            real_name,
            user_name,
            password,
        )
        session["user_id"] = db.execute(
            "SELECT id FROM users WHERE user_name = ?", user_name
        )[0]["id"]
        session["user_name"] = user_name
        session["real_name"] = real_name
        return redirect("/login")


@app.route("/grades", methods=["GET", "POST"])
@login_required
def grades():
    if request.method == "GET":
        grades = db.execute(
            "SELECT * FROM grades where user_id = ?", session["user_id"]
        )
        return render_template("grades.html", grades=grades)

    elif request.method == "POST":
        None


@app.route("/add_subject", methods=["POST", "GET"])
@login_required
def add_subject():
    if request.method == "POST":
        subjects = db.execute(
            "SELECT subject FROM grades WHERE user_id = ?", session["user_id"]
        )
        added_subject = request.form.get("added_subject")
        for subject in subjects:
            subject = subject["subject"]
            if subject == added_subject.lower():
                return fault("Subject already exists!")

        db.execute(
            "INSERT INTO grades (user_id, subject) VALUES (?, ?)",
            session["user_id"],
            added_subject.lower(),
        )

        grades = db.execute(
            "SELECT * FROM grades where user_id = ?", session["user_id"]
        )
        return render_template("grades.html", grades=grades)

    if request.method == "GET":
        None


@app.route("/add_to_grade", methods=["POST"])
@login_required
def add_to_grade():
    subject = request.form.get("subject_selector")
    if subject == "add_subject":
        return add_subject()
    current = db.execute(
        "SELECT * FROM grades WHERE user_id = ? AND subject = ?;",
        session["user_id"],
        subject.lower(),
    )[0]
    for key in current:
        if current[key] == "":
            current[key] = 0

    oral = request.form.get("oral_grade")
    try:
        oral = float(oral)
    except ValueError:
        return render_template("Invalid oral Grade!")
    print(oral)
    if oral > 6 or oral < 1:
        return fault("Invalid oral Grade!")
    new_oral = ((current["oral"] * current["input_count"]) + oral) / (
        current["input_count"] + 1
    )

    written = request.form.get("written_grade")
    try:
        written = float(written)
    except ValueError:
        return render_template("Invalid written Grade!")
    if written > 6 or written < 1:
        return fault("Invalid Written Grade!")
    new_written = ((current["written"] * current["input_count"]) + written) / (
        current["input_count"] + 1
    )

    grade = request.form.get("grade")
    try:
        grade = float(grade)
    except ValueError:
        return render_template("Invalid Grade!")
    if grade > 6 or grade < 1:
        return fault("Invalid Grade!")
    new_grade = ((current["grade"] * current["input_count"]) + grade) / (
        current["input_count"] + 1
    )

    db.execute(
        "UPDATE grades SET oral = ?, written = ?, grade = ?, input_count = ? WHERE subject = ? AND user_id = ?;",
        new_oral,
        new_written,
        new_grade,
        current["input_count"] + 1,
        subject,
        session["user_id"],
    )
    return redirect("/")


def fault(message):
    return render_template("fault.html", message=message)
