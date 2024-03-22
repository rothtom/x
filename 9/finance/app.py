import os
import datetime
import re

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    user_id = int(session["user_id"])
    purchase_dict_list = db.execute(
        "SELECT stock_name as name, shares FROM purchases WHERE user_id = ?", user_id
    )
    stock_value = 0
    for purchase_dict in purchase_dict_list:
        if "price" not in purchase_dict.keys():
            lookup_price = float(lookup(purchase_dict["name"])["price"])
            purchase_dict["price"] = lookup_price
        purchase_dict["total"] = purchase_dict["shares"] * lookup_price
        stock_value += purchase_dict["total"]

    for dict in purchase_dict_list:
        dict["total"] = usd(dict["total"])
        dict["price"] = usd(dict["price"])

    cash = db.execute("SELECT cash FROM users WHERE id = ?;", user_id)[0]["cash"]
    total_value = cash + stock_value
    return render_template(
        "index.html",
        stocks=purchase_dict_list,
        stock_value=usd(stock_value),
        cash=usd(cash),
        total_value=usd(total_value),
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")

    elif request.method == "POST":
        symbol = request.form.get("symbol")
        stock_dict = lookup(symbol)
        if symbol and stock_dict:
            stock_dict["usd"] = usd(stock_dict["price"])
            # return render_template("quoted.html", stock_dict = stock_dict) stupid?
        else:
            return apology("Invalid Stock name")

        shares = request.form.get("shares")

        try:
            shares = int(shares)
        except ValueError:
            return apology("Invalid share number!")

        if shares < 1:
            return apology("Must buy at least 1 share!")

        user_id = session["user_id"]
        cash_now = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        price = float(stock_dict["price"]) * shares
        buy_time_stamp = datetime.datetime.now()
        if cash_now < price:
            return apology("Not enough cash!")
        remaining_cash = cash_now - price
        db.execute("UPDATE users SET cash = ? WHERE id = ?;", remaining_cash, user_id)
        purchase_dict = db.execute("SELECT * FROM purchases WHERE user_id = ?", user_id)
        print(purchase_dict)

        purchase_names = []
        for purchase in purchase_dict:
            purchase_names.append(purchase["stock_name"])
        if stock_dict["name"] in purchase_names:
            purchase["shares"] += shares
            db.execute(
                "UPDATE purchases SET shares = ? WHERE stock_name = ? AND user_id = ?;",
                purchase["shares"],
                purchase["stock_name"],
                user_id,
            )
        else:
            purchase_dict = {"stock_name": stock_dict["name"], "shares": shares}
            db.execute(
                "INSERT INTO purchases (user_id, stock_name, shares) VALUES (?, ?, ?);",
                user_id,
                purchase_dict["stock_name"],
                purchase_dict["shares"],
            )

        db.execute(
            "INSERT INTO history (user_id, name, shares, stock_price, value, time_stamp, trans_type) VALUES (?, ?, ?, ?, ?, ?, 'buy');",
            user_id,
            symbol,
            shares,
            stock_dict["price"],
            price,
            buy_time_stamp,
        )

        # return redirect("/")
        return render_template(
            "bought.html", stock=stock_dict, total=("%.2f" % price), shares=shares
        )  # would be nice but not required


@app.route("/history")
@login_required
def history():
    stocks_dict = db.execute(
        "SELECT name, shares ,stock_price, value, time_stamp, trans_type FROM history WHERE user_id = ?;",
        session["user_id"],
    )
    for stock_dict in stocks_dict:
        stock_dict["value"] = usd(stock_dict["value"])
        stock_dict["stock_price"] = usd(stock_dict["stock_price"])
    return render_template("history.html", stocks=stocks_dict)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")

    elif request.method == "POST":
        symbol = request.form.get("symbol")
        stock_dict = lookup(symbol)
        if symbol and stock_dict:
            stock_dict["usd"] = usd(stock_dict["price"])
            return render_template("quoted.html", stock_dict=stock_dict)
        else:
            return apology("Invalid Stock name")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("username")

        if name == "":
            return apology("Must provide username!")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        print(f"Password: {password}")
        if password == "" or confirmation == "":
            return apology("Must provide password!")
        names = db.execute("SELECT username FROM users WHERE username = ?;", name)
        for username in names:
            if name == username["username"]:
                return apology("username is already taken!")

        if password != confirmation:
            return apology("Password didnt match Confirm Password")

        if _ := not re.search("[a-zA-Z]*[0-9]+[a-zA-Z]*", password) and re.search(
            "[0-9]+", password
        ):
            return apology("Password must contain numbers and chars!")

        hashed_password = generate_password_hash(password, method="pbkdf2")
        db.execute(
            "INSERT INTO users (username, hash)  VALUES (?, ?);", name, hashed_password
        )

        return redirect("/")

    if request.method == "GET":
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        share_symbols = db.execute(
            "SELECT stock_name as name FROM purchases WHERE user_id = ?;",
            session["user_id"],
        )
        symbol_list = []
        for symbol in share_symbols:
            symbol_list.append(symbol["name"])
        return render_template("sell.html", stocks=symbol_list)

    elif request.method == "POST":
        user_id = session["user_id"]

        name = request.form.get("symbol")
        shares = request.form.get("shares")

        try:
            shares = int(shares)
        except ValueError:
            return apology("Shares must be a whole number")

        available_shares = db.execute(
            "SELECT shares FROM purchases WHERE user_id = ? AND stock_name = ?;",
            user_id,
            name,
        )[0]["shares"]

        if available_shares and (shares <= available_shares):
            price = lookup(name)["price"]
            print(f"lookup: {price}, shares: {shares}")
            value = shares * price
            cash = float(
                db.execute("SELECT cash FROM users WHERE id = ?;", user_id)[0]["cash"]
            )

            remaining_cash = cash + value
            db.execute(
                "UPDATE users SET cash = ? WHERE id = ?;", remaining_cash, user_id
            )
            remaining_shares = available_shares - shares
            db.execute(
                "UPDATE purchases SET shares = ? WHERE user_id = ? AND stock_name = ?;",
                remaining_shares,
                user_id,
                name,
            )
            sell_time_stamp = datetime.datetime.now()

            if (
                db.execute(
                    "SELECT shares FROM purchases WHERE user_id = ? AND stock_name = ?;",
                    user_id,
                    name,
                )[0]["shares"]
                == 0
            ):
                db.execute(
                    "DELETE FROM purchases WHERE user_id = ? AND stock_name = ?;",
                    user_id,
                    name,
                )

            db.execute(
                "INSERT INTO history (user_id, name, shares, stock_price, value, time_stamp, trans_type) VALUES (?, ?, ?, ?, ?, ?,'sell');",
                user_id,
                name,
                shares,
                price,
                value,
                sell_time_stamp,
            )
            return redirect("/")
            return render_template(
                "sold.html",
                name=name,
                shares=shares,
                price=usd(price),
                total=usd(value),
                cash=usd(remaining_cash),
            )  # not a specification

        else:
            return apology("Not enough shares to sell!")
