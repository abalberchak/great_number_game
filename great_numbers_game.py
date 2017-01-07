from flask import Flask, render_template, request, redirect, session, Markup
app = Flask(__name__)
app.secret_key = 'SECRET'
import random


	# def initialize():
	# import random
	# session['target'] = random.randrange(0, 101)
	# #print session['session['target']']
	#  return session['target']


@app.route('/')
def index():
	if not 'target' in session:
		session['target'] = random.randrange(0, 101)
	return render_template("index.html", msg=session['msg'])
 	

@app.route('/SubmitNumber', methods=['POST'])
def SubmitNumber():
	session['number'] = request.form['number']
	
	
	# return session['target']
	if session['number'].isdigit() == False:
		session['msg'] = Markup("<div class='msg_box red'><h3>That isn't a Number! Please enter a valid number!</h3></div>")

 	elif session['target'] == int(session['number']):
 		# print str(session['session['target']']) + " was the number!"
 		session['msg'] = Markup("<div class='msg_box green'><h3>" + str(session['target']) + " was the number!</h3><form action='/reset' method='get'><button id='button' type='submit'>Play Again!</button></form></div>")
 		print session['target']


 	elif session['target'] < int(session['number']):
 		print "Too high!"
 		session['msg'] = Markup("<h3 class='msg_box red'>Too high!</h3>")
 		print session['target']

 	elif session['target'] > int(session['number']):
 		print "Too low!"
 		session['msg'] = Markup("<h3 class='msg_box red'>Too low!<h3>")
 		print session['target']

	return redirect('/')

@app.route('/reset')
def reset():
	session['msg'] = ''
	session.pop('target')
	return redirect('/')


app.run(debug=True) 
