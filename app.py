from flask import Flask, Response, render_template, request

app = Flask(__name__, static_folder="static", static_path="")

@app.route('/', methods=['GET', 'POST'])
def index():
	title="STOCKHOLM"
	return render_template('index.html', title=title)

@app.route('/about/')
def about():
	return render_template('about.html')

if __name__=='__main__':
	app.run(port=5000, debug=True)

