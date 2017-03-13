from flask import Flask, request, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'login')
app.secret_key = 'password'
EMAIL_REGEX = re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name = re.compile(r'^[a-zA-Z]')

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
	error = 0
	query = 'SELECT id, pw_has FROM login WHERE email_add = "{}"'.format(request.form['username'])
	user = mysql.query_db(query)
	
	if len(user) < 1:
		error +=1
		return redirect('/failure')
	elif not bcrypt.check_password_hash(user[0]['pw_has'], request.form['password2']):
		error +=1
		return redirect('/failure')
	else: 
		return redirect('/success')

	return redirect('/')

@app.route('/register', methods=['POST'])
def register():
	error = 0
	if len(request.form['first_name'])<2:
		error += 1
		flash("Need more Charecters")
	elif not name.match(request.form['first_name']):
		error += 1
		flash('No Numbers Allowed in Name')
	if len(request.form['last_name'])<2:
		error += 1
		flash('Need more Charecters')
	elif not name.match(request.form['last_name']):
		error += 1
		flash('No Numbers Allowed in Name')
	if not EMAIL_REGEX.match(request.form['email_add']):
		error +=1
		flash('Email is Not Valid')
	if len(request.form['password']) < 9:
		error += 1
		flash('Password needs to be 9 charecters or more!')
	if request.form['password'] != request.form['confirm']:
		error += 1
		flash('Passwords Do Not Match!')
	
	if error == 0:
		hashed = bcrypt.generate_password_hash(request.form['password'])
		query = 'INSERT INTO login (first_name, last_name, email_add, pw_has, created_at, updated_at) VALUES (:first_name, :last_name, :email_add, :pw_has, NOW(), NOW())'
		data = {'first_name': request.form['first_name'], 'last_name': request.form['last_name'], 'email_add': request.form['email_add'], 'pw_has': hashed }
		mysql.query_db(query, data)
		return redirect('/success')

	return redirect('/')


@app.route('/success')
def success():

	return render_template('success.html')


@app.route('/failure')
def failure():

	return render_template('failed.html')

@app.route('/goback', methods=['POST'])
def goback():
	return redirect('/')

app.run(debug=True)
