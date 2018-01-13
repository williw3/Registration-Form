from flask import Flask, render_template, redirect, request, session, flash
import re
import time 
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')


@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit():
	birthday = request.form['bday']
	print birthday
	#name val
	if len(request.form['firstname']) < 1 or len(request.form['lastname']) < 1:
		flash('Name cannot be blank', 'error')
	elif not (request.form['firstname']).isalpha() or not (request.form['lastname']).isalpha():
		flash('Name cannot contain numbers or spaces', 'error')

	#email val
	if len(request.form['email']) < 1:  
		flash('Email cannont be blank', 'error')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid Email Address!', 'error')
	
	#password val
	if len(request.form['password']) < 8:
		flash('Password must contain at least 8 characters', 'error')
	elif request.form['password'] != request.form['password_confirm']:
		flash('Passwords do not match', 'error')

	#birthday val
	if birthday > stamp:
		flash('Please enter valid birthday', 'error')

	else:
		flash('Success! Congratulations {} {}. You have registered with email {} at {}'.format(request.form['firstname'], request.form['lastname'], request.form['email'], stamp), 'success')


	return redirect('/')


app.run(debug=True)