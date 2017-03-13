from flask import Flask
app = Flask(__name__)
@app.route('/')
def __init__(self, app, db):
	config = {
		'host': 'localhost',
		'database': db,
		'user': 'root',
		'password': 'root',
		'port': '8889'

	}




app.run(debug=True)