from flask import Flask, Response, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__, static_folder="static", static_path="")
DB_FILE="mydb"

comments = []

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
		return render_template("guestbook.html", comments=comments)
	comments.append(request.form["commentContent"])
	return redirect(url_for('guestbook'))




@app.route('/resultTest',methods = ['POST', 'GET'])
def resultTest():
	if request.method == 'POST':
		result = request.form['comment']
		print(result)
		return render_template("resultTest.html", result = result)



if __name__=='__main__':
	app.run(port=5000, debug=True)
