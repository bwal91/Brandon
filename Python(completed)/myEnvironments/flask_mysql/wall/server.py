from flask import Flask, request, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'wall')
app.secret_key = 'password'
EMAIL_REGEX = re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name = re.compile(r'^[a-zA-Z]')

@app.route('/')
def index():
	try:
		session['user_id']==""
	except KeyError: 
		session['user_id']=""

	return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
	error = 0
	query = 'SELECT id, first_name, password FROM users WHERE email = "{}"'.format(request.form['username'])
	user = mysql.query_db(query)
	
	if len(user) < 1:
		error +=1
		return redirect('/failure')
	elif not bcrypt.check_password_hash(user[0]['password'], request.form['password2']):
		error +=1
		return redirect('/failure')
	else: 
		session['user_id']=user[0]['id']
		print user
		return redirect('/wall')
	
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
		query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())'
		data = {'first_name': request.form['first_name'], 'last_name': request.form['last_name'], 'email': request.form['email_add'], 'password': hashed }
		mysql.query_db(query, data)
		return redirect('/wall')

	return redirect('/')

@app.route('/wall')
def wall():
	query = "SELECT first_name FROM users WHERE id = '{}'".format(session['user_id'])
	qfirst = mysql.query_db(query)
	
	query = "SELECT messages.id, messages.message, messages.created_at, users.first_name, users.last_name FROM messages JOIN users on users.id = messages.users_id"
	all_messages = mysql.query_db(query)
	
	query = "SELECT comments.messages_id, comments.comment, comments.created_at, users.first_name, users.last_name FROM comments JOIN users on users.id = comments.users_id"
	all_comments = mysql.query_db(query)

	return render_template('wall.html', first_name=qfirst[0]['first_name'], messages=all_messages, comments=all_comments)

@app.route('/message', methods=['POST'])
def message():
	query = "INSERT INTO messages (message, created_at, updated_at, users_id) VALUES (:message, NOW(), NOW(), :users_id)"
	data = {
			'message': request.form['content'],
			'users_id': session['user_id']
		}
	mysql.query_db(query, data)
	return redirect('/wall')


@app.route('/comment/<message_id>', methods=['POST'])
def comment(message_id):
	query = "INSERT INTO comments (comment, created_at, updated_at, users_id, messages_id) VALUES (:comment, NOW(), NOW(), :users_id, :messages_id)"
	data = {
			'comment': request.form['ccontent'],
			'users_id': session['user_id'],
			'messages_id': message_id
		}
	mysql.query_db(query, data)
	return redirect('/wall')

@app.route('/logoff')
def lofoff():
	session.clear()
	return redirect('/')


@app.route('/failure')
def failure():	
	return render_template('failed.html')

@app.route('/goback', methods=['POST'])
def goback():
	return redirect('/')






app.run(debug=True)
