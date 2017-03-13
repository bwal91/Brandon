from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/survey', methods=['POST'])
def submit():
   	first = request.form['Your_Name']
   	location = request.form['location']
   	language = request.form['language']
   	comment = request.form['com']
   	return render_template("submitted.html", name=first, loc=location, fav=language, comments=comment)
@app.route('/goback', methods=['POST'])
def goback():	
	return redirect('/')
app.run(debug=True)