from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key = 'Brandon'
@app.route('/')
def index():
	if not 'number' in session:
		session['number']=random.randrange(0, 101)
	if not 'result' in session:
		session ['result']=-1
		print session['result']
	return render_template("index.html", number=session['number'])

@app.route('/box', methods=['POST'])
def guess():
	if request.form['box']=="":
		session.clear()
		return redirect('/')
	session['result']=int(request.form['box'])
	return redirect('/')
app.run(debug=True)