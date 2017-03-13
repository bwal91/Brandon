from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'mydb')
app.secret_key = 'Brandon'

@app.route('/')
def index():
    if not 'email' in session:
        session['email']=''
    if not 'valid' in session:
        session['valid']='invalid'
    query = "SELECT * FROM Emails"
    emails = mysql.query_db(query)
    return render_template("index.html", emails=emails)

@app.route('/validate', methods=['POST'])
def em():
	match=re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", request.form['email'])
	if match:
		session['email']= request.form['email']
		session['valid']='valid'
		create() 
	else:
		session['valid']='invalid'
	return redirect('/')
def create():
	query = "INSERT INTO Emails (emails, created_at) VALUES (:emails, NOW())"	
	data = {'emails': request.form['email']}
	mysql.query_db(query, data)
	

app.run(debug=True)