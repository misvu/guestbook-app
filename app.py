from flask import Flask, Response, render_template, request, redirect, url_for
from flask import g
import sys
import sqlite3

app = Flask(__name__, static_folder="static", static_path="")
DB_FILE="guestbook"

comments = []

def insert_comment(name, comment):
	cursor = g.db.cursor()
	cursor.execute("INSERT INTO comment(name, comment, DATE) values(?,?, date('now'))", (name, comment))
	g.db.commit()

def fetch_all_comment():
	cursor = g.db.cursor()
	cursor.execute("SELECT name, comment, date from comment")
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
	title="STOCKHOLM"
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


@app.route('/guestbook',methods = ['POST', 'GET'])
def guestbook():
	if request.method == "GET":
		return render_template("guestbook.html", comments=fetch_all_comment())

	comment = request.form["commentContent"]
	name = request.form["name"]
	insert_comment(name, comment)
	return redirect(url_for('guestbook'))




@app.route('/resultTest',methods = ['POST', 'GET'])
def resultTest():
	if request.method == 'POST':
		result = request.form['comment']
		print(result)
		return render_template("resultTest.html", result = result)



if __name__=='__main__':
	app.run(port=5000, debug=True)
