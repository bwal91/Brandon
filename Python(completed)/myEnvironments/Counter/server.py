from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'Brandon'
@app.route('/')
def index():
	try:
		session['count']+=1
	except KeyError:
		session['count'] = 1
	return render_template("index.html")
@app.route('/button', methods=["POST"])
def submit():
	session.clear()
	return redirect('/')
app.run(debug=True)