from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'usethis')
app.secret_key = 'Brandon'

@app.route('/')
def index():
	query = "SELECT * FROM Friends"
	friends = mysql.query_db(query)
	return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
	query = "INSERT INTO Friends (first_name, last_name, email_add, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
	data = {
            'first_name': request.form['first'], 
            'last_name':  request.form['last'],
            'email': request.form['email']
           }
	mysql.query_db(query, data)
	return redirect('/')


@app.route('/friends/<id>/edit')
def edit(id):
	query = "SELECT * FROM Friends WHERE id = :specific_id"
	data = {'specific_id': id}
	friends = mysql.query_db(query, data)
	return render_template('edit.html', one_friend=friends[0])

@app.route('/friends/<id>', methods=['POST'])
def update(id):
	query = "UPDATE Friends SET first_name = :first_name, last_name = :last_name, email_add = :email WHERE id = :specific_id"
	data = {
             'first_name': request.form['first_name'], 
             'last_name':  request.form['last_name'],
             'email': request.form['email_add'],
             'specific_id': id
           }
	mysql.query_db(query, data)
	return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
	query = "DELETE FROM friends WHERE id = :id"
	data = {'id': id}
	mysql.query_db(query, data)
	return redirect('/')

app.run(debug=True)