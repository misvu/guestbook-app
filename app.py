from flask import Flask, render_template, request, redirect, url_for, flash
import os
from flask import g
import sqlite3

app = Flask(__name__, static_folder="static", static_path="")

# Secret key is needed to keep the client-side sessions secure
# os.urandom(n) returns a string of n random bytes
app.secret_key = os.urandom(24)

DB_FILE = "guestbook"

comments = []


def insert_comment(name, comment):
    cursor = g.db.cursor()
    cursor.execute("INSERT INTO comment(name, comment, DATE) values(?,?, date('now'))", (name, comment))
    g.db.commit()


def fetch_all_comment():
    cursor = g.db.cursor()
    cursor.execute("SELECT name, comment, date FROM comment")
    return list(cursor.fetchall())


def fetch_all_users():
    cursor = g.db.cursor()
    cursor.execute("SELECT username FROM USER")
    return list(cursor.fetchall())


@app.before_request
def before_request():
    g.db = sqlite3.connect('guestbook.db')


@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route('/')
def index():
    title = "STOCKHOLM"
    return render_template('index.html', title=title)


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/eat/')
def eat():
    return render_template('eat.html')


@app.route('/sightseeing/')
def sightseeing():
    return render_template('sightseeing.html')


@app.route('/guestbook')
def guestbook():
    return render_template("guestbook.html")


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "POST":
        username = request.form["usernm"]
        password = request.form["passwd"]
        cursor = g.db.cursor()
        try:
            cursor.execute("SELECT USERNAME FROM USER WHERE USERNAME=?", (username))
            if cursor.fetchone() == None:
                flash("No user with that name")
                return redirect(url_for("login"))
            elif password != cursor.execute("SELECT PASSWORD FROM USER WHERE USERNAME=?", (username)):
                flash("Wrong password!")
                return redirect(url_for("login"))
            flash("Logged in sucessfully")
            return redirect(url_for("guestbook-loggedin"))
        except sqlite3.IntegrityError:
            flash("error")
            return render_template("login.html")
    return render_template("login.html")




@app.route('/guestbook-loggedin', methods=['GET', 'POST'])
def guestbookloggedin():
    if request.method == "GET":
        user = {'nickname': 'Anna'}
        return render_template('guestbook-loggedin.html', comments=fetch_all_comment(), user=user)
    name = request.form["name"]
    comment = request.form["commentContent"]
    insert_comment(name, comment)
    return redirect(url_for('guestbookloggedin'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('register.html', users=fetch_all_users())
    try:
        name = request.form["name"]
        username = request.form["username"]
        city = request.form["city"]
        password = request.form["pwd"]
        cursor = g.db.cursor()

        cursor.execute("INSERT INTO USER (name, username, city, password) VALUES(?, ?, ?, ?)",
                       (name, username, city, password))
        g.db.commit()
        flash("Successfully registered")
        return redirect(url_for("guestbookloggedin"))
    except sqlite3.IntegrityError:
        flash("Error in registration form!")
        return redirect(url_for("register"))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
