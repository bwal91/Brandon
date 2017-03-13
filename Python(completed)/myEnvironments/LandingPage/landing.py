from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def landing():
	return render_template('land.html')
@app.route('/ninjas')
def ninja():
	return render_template('landninja.html')
@app.route('/dojos/new')
def dojo():
	return render_template('landdojos.html')
app.run(debug=True)