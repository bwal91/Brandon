from flask import Flask, render_template, session, redirect, request
import random
app=Flask(__name__)
app.secret_key = 'Brandon'
@app.route('/')
def index():
	if not 'gold' in session:
		session['gold']=0
	if not 'res' in session:
		session['res']=0
	if not 'acti' in session:
		session['acti']=[]
	return render_template('index.html')
@app.route('/process_money', methods=['POST'])
def gold():
	if request.form['building']=='farm':
		session['']=0
		session['res']=session['res']+random.randrange(10,21)
		session['gold']=session['gold']+session['res']
		session['where']='Farm'
	elif request.form['building']=='cave':
		session['res']=0
		session['res']=session['res']+random.randrange(-4, 11)
		session['gold']=session['gold']+session['res']
		session['where']='Caves'
	elif request.form['building']=='house':
		session['res']=0
		session['res']=session['res']+random.randrange(9, 21)
		session['gold']=session['gold']+session['res']
		session['where']='House'
	elif request.form['building']=='casino':
		session['res']=0
		session['res']=session['res']+random.randrange(-51, 51)
		session['gold']=session['gold']+session['res']
		session['where']='Casino'
	else:
		print "You Lose"
	
	comments()
	return redirect('/')
def comments():
	session['acti'].append('You earned ' + str(session['res'])+ ' gold from the '+ str(session['where'])+'!'+)
	
	return redirect('/')

app.run(debug=True) 