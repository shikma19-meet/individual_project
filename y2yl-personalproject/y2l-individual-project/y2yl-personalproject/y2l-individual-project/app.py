from flask import Flask, render_template, request, redirect, url_for
from database import *
import database 
app = Flask(__name__)



@app.route('/')
def home():
	all_charities = database.get_all_charities()
	# if request.method == 'GET':
	return render_template('home.html',all_charities = all_charities)

@app.route('/add_charity',methods =['GET', 'POST'])
def add_charity():
	if request.method == 'GET':
		return render_template('add_charity.html')
	if request.method == 'POST': 
		database.add_charity(request.form['charity_name'],
			request.form['short_description'],
			request.form['url'],
			request.form['pic1'],
			request.form['pic2'],
			request.form['pic3'])
		return redirect(url_for('home'))


@app.route('/charities/<int:id>')
def charity_page(id):
	charity = get_one_charity(id)
	return render_template('charity_page.html',charity = charity)
   
if __name__ == '__main__':
    app.run(debug=True)

